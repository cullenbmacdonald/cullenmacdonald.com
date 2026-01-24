# Cullen MacDonald's Personal Website

This repository contains the source code for [cullenmacdonald.com](https://cullenmacdonald.com), a personal website and blog built with Hugo.

## Overview

This project uses Hugo as a static site generator and integrates with an Obsidian vault to publish blog posts. The site features:

- Personal landing page with contact links
- Blog hosted at [blog.cullenmacdonald.com](https://blog.cullenmacdonald.com)
- Automated content syncing from Obsidian notes

## Prerequisites

- [Hugo](https://gohugo.io/) - Static site generator
- [Pandoc](https://pandoc.org/) - Document converter
- [Pipenv](https://pipenv.pypa.io/) - Python dependency management
- [Homebrew](https://brew.sh/) - Package manager (for macOS)

## Installation

Install all required dependencies:

```bash
make install
```

This will install Hugo, Pandoc, and Python dependencies via Pipenv.

## Development

### Local Development Server

Run the Hugo development server with draft content:

```bash
make dev
```

The site will be available at `http://localhost:1313`.

### Update Content from Obsidian

Sync content from your Obsidian vault to the Hugo content directory:

```bash
make update-content
```

This runs `copy_from_vault.py`, which:
- Copies markdown files tagged with `#blog/publish` from your Obsidian vault
- Converts Obsidian-style metadata to Hugo front matter
- Converts internal `[[wiki-links]]` to standard markdown links
- Copies referenced images to the content directory

### Build the Site

Build the production site:

```bash
make build-site
```

This command:
- Builds the Hugo site with minification
- Cleans the `docs/` directory (preserving the CNAME file)
- Moves the built site from `public/` to `docs/` for GitHub Pages deployment

## Project Structure

- `content/` - Hugo content directory
- `layouts/` - Hugo layout templates
- `static/` - Static assets
- `docs/` - Built site (published to GitHub Pages)
- `archetypes/` - Hugo content templates
- `copy_from_vault.py` - Script to sync content from Obsidian
- `hugo.toml` - Hugo configuration
- `index.html` - Landing page

## Deployment

The site is deployed via GitHub Pages from the `docs/` directory.

## Configuration

Update site settings in `hugo.toml`:
- `baseURL` - Site URL
- `title` - Site title
- Additional Hugo configuration options

## License

Personal website content - all rights reserved.
