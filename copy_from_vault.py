"""
Import notes from the Obsidian vault into Hugo content.

A note is published when it contains the #blog/publish tag. Notes that also
carry #blog/one-small-thing go into the One Small Thing series and get numbered
by date. Everything else becomes a regular post at the content root.

Obsidian note shape:

    # Title

    body...

    ---
    Tags: #blog/publish #blog/one-small-thing
    Created: [[2026-09-28]]
    Description: optional one-line summary for link previews

Usage:
    python copy_from_vault.py [--dry-run] [--prune]

Set VAULT to override the vault location.
"""

import argparse
import os
import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import frontmatter

REPO = Path(__file__).resolve().parent
VAULT = Path(os.getenv("VAULT", "~/personal notes")).expanduser()
CONTENT = REPO / "content"
SERIES_SECTION = "one-small-thing"
IMAGES = REPO / "static" / "images"

PUBLISH_TAG = "#blog/publish"
SERIES_TAG = "#blog/one-small-thing"
SKIP_DIRS = {".obsidian", ".trash", ".git"}

H1 = re.compile(r"^# (.+)\n", re.MULTILINE)
FOOTER = re.compile(r"\n---\s*\n((?:[A-Za-z ]+:.*(?:\n|$))+)\s*\Z")
EMBED = re.compile(r"!\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
TAG_ONLY_LINE = re.compile(r"^\s*(#[\w/-]+\s*)+$", re.MULTILINE)


@dataclass
class Note:
    source: Path
    slug: str
    series: bool
    title: str = ""
    date: datetime | None = None
    description: str = ""
    body: str = ""
    number: int | None = None
    images: list[str] = field(default_factory=list)

    @property
    def dest(self) -> Path:
        folder = CONTENT / SERIES_SECTION if self.series else CONTENT
        return folder / f"{self.slug}.md"

    @property
    def url(self) -> str:
        return f"/{SERIES_SECTION}/{self.slug}/" if self.series else f"/{self.slug}/"


def slugify(name: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", name.lower())
    return re.sub(r"[\s_]+", "-", slug).strip("-")


def find_notes(vault: Path) -> list[Note]:
    notes = []
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if not name.endswith(".md"):
                continue
            path = Path(root) / name
            text = path.read_text(encoding="utf-8")
            if PUBLISH_TAG not in text:
                continue
            notes.append(Note(source=path, slug=slugify(path.stem), series=SERIES_TAG in text))
    return notes


def parse(note: Note) -> None:
    text = note.source.read_text(encoding="utf-8")

    footer = FOOTER.search(text)
    if footer:
        text = text[: footer.start()]
        for line in footer.group(1).splitlines():
            key, _, value = line.partition(":")
            key, value = key.strip().lower(), value.strip()
            if key == "created" and value:
                note.date = datetime.strptime(value.strip("[]"), "%Y-%m-%d")
            elif key == "description":
                note.description = value

    h1 = H1.search(text)
    note.title = h1.group(1).strip() if h1 else note.source.stem
    if h1:
        text = text[: h1.start()] + text[h1.end() :]

    note.body = TAG_ONLY_LINE.sub("", text).strip() + "\n"


def resolve_links(note: Note, published: dict[str, Note]) -> None:
    """Embeds become images; wikilinks to published notes become links, the rest plain text."""

    def embed(match):
        name = match.group(1).strip()
        note.images.append(name)
        return f"![{Path(name).stem}](/images/{name.replace(' ', '%20')})"

    def link(match):
        target, anchor, alias = match.group(1).strip(), match.group(2) or "", match.group(3)
        text = alias or target
        dest = published.get(target.lower())
        if not dest:
            return text
        return f"[{text}]({dest.url}{'#' + slugify(anchor[1:]) if anchor else ''})"

    note.body = EMBED.sub(embed, note.body)
    note.body = WIKILINK.sub(link, note.body)


def render(note: Note) -> str:
    post = frontmatter.Post(note.body)
    post["title"] = note.title
    if note.date:
        post["date"] = note.date.date()
    if note.description:
        post["description"] = note.description
    if note.number:
        post["number"] = note.number
    return frontmatter.dumps(post, sort_keys=False) + "\n"


def copy_images(note: Note, vault: Path, dry_run: bool) -> None:
    for name in note.images:
        matches = [p for p in vault.rglob(Path(name).name) if ".trash" not in p.parts]
        if not matches:
            print(f"  ! missing image {name} in {note.source.name}")
            continue
        if not dry_run:
            IMAGES.mkdir(parents=True, exist_ok=True)
            shutil.copy(matches[0], IMAGES / name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="show what would change without writing")
    parser.add_argument("--prune", action="store_true", help="delete content files with no published note behind them")
    args = parser.parse_args()

    if not VAULT.is_dir():
        raise SystemExit(f"vault not found: {VAULT} (set VAULT=...)")

    notes = find_notes(VAULT)
    for note in notes:
        parse(note)

    missing_dates = [n.source.name for n in notes if n.series and not n.date]
    if missing_dates:
        raise SystemExit(f"series notes need a Created date to be numbered: {', '.join(missing_dates)}")
    series = sorted((n for n in notes if n.series), key=lambda n: n.date)
    for number, note in enumerate(series, start=1):
        note.number = number

    published = {n.source.stem.lower(): n for n in notes}
    for note in notes:
        resolve_links(note, published)

    for note in sorted(notes, key=lambda n: (not n.series, n.number or 0, n.slug)):
        rendered = render(note)
        existing = note.dest.read_text(encoding="utf-8") if note.dest.exists() else None
        status = "new" if existing is None else "unchanged" if existing == rendered else "updated"
        label = f"#{note.number} " if note.number else ""
        print(f"{status:>9}  {note.dest.relative_to(REPO)}  ({label}{note.title})")
        if status != "unchanged" and not args.dry_run:
            note.dest.parent.mkdir(parents=True, exist_ok=True)
            note.dest.write_text(rendered, encoding="utf-8")
        copy_images(note, VAULT, args.dry_run)

    expected = {n.dest for n in notes}
    for path in sorted(CONTENT.rglob("*.md")):
        if path.name.startswith("_index") or path in expected or frontmatter.load(path).get("manual"):
            continue
        action = "removing" if args.prune and not args.dry_run else "orphan"
        print(f"{action:>9}  {path.relative_to(REPO)}  (no #blog/publish note in vault)")
        if args.prune and not args.dry_run:
            path.unlink()

    if args.dry_run:
        print("\ndry run: nothing written")


if __name__ == "__main__":
    main()
