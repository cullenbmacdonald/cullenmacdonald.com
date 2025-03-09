import os
from datetime import datetime
import shutil
from pathlib import Path
import re
import glob
from typing import Tuple

import pandoc
from pandoc.types import *
import frontmatter

git = os.getenv("git")
secondbrain = "/Users/cmacdonald/Documents/personal notes"
secondbrain_public = "/Users/cmacdonald/dev/cullenmacdonald.com/content"

FRONTMATTER_KEYS = ["Created"]

# define paths
second_brain_path = str(secondbrain)  # "/tmp/second-brain-tmp"
public_folder_path_copy = str(secondbrain_public)
public_brain_image_path = os.path.join(public_folder_path_copy, "images")

regexp_md_images = "!\[\[(.*?)\]\](.*)\s"
h1 = "(?m)^#(?!#)(.*)"

def process_file(original_file_path: str, copied_file_path: str) -> None:
    convert_to_frontmatter(copied_file_path)
    convert_internal_links(copied_file_path)
    list_images_from_markdown(original_file_path)

def convert_to_frontmatter(file_path):
    """
    Convert Obsidian-style metadata to Hugo front matter in a markdown file.

    Parameters:
        file_path (str): The path to the markdown file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the H1 title
    h1_match = re.search(r'^# (.+)', content, re.MULTILINE)
    title = h1_match.group(1) if h1_match else None
    content = re.sub(r'^# .+\n', '', content, 1) if title else content

    # Extract the bottom metadata block
    metadata_match = re.search(r'(?s)---\n(.*?)\Z', content)
    metadata = {}
    if metadata_match:
        metadata_block = metadata_match.group(1)
        # Parse the metadata block into a dictionary
        for line in metadata_block.splitlines():
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()
            if key in FRONTMATTER_KEYS:
                if key == "Created":
                    # Remove brackets from [[YYYY-MM-DD]] format
                    value = datetime.strptime(re.sub(r'\[\[(.*?)\]\]', r'\1', value), "%Y-%m-%d")
                    key = "date"
                metadata[key] = value
        # Remove the metadata block from the content
        content = content[:metadata_match.start()] + content[metadata_match.end():]

    # Prepare the front matter
    fm = frontmatter.loads('')
    if title:
        fm['title'] = title
    for key, value in metadata.items():
        fm[key] = value

    # Combine the new front matter and content
    fm.content = content.strip()
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(fm))

    print(f"Converted file: {file_path}")

def convert_internal_links(file_path: str) -> None:
    """
    Convert Obsidian-style internal links [[Document Name]] to standard markdown links.
    
    Parameters:
        file_path (str): The path to the markdown file.
    """
    # Use absolute path to ensure correct path handling
    print(f"Processing existing file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Handle links with custom text: [[Document Name|custom text]]
    def replace_custom_link(match):
        doc_name = match.group(1).lower().replace(" ", "-")
        link_text = match.group(2)
        return f'[{link_text}](/{doc_name})'
    
    # Handle standard links: [[Document Name]]
    def replace_standard_link(match):
        doc_name = match.group(1)
        doc_path = doc_name.lower().replace(" ", "-")
        return f'[{doc_name}](/{doc_path})'
    
    # Apply replacements
    content = re.sub(r'\[\[(.*?)\|(.*?)\]\]', replace_custom_link, content)
    content = re.sub(r'\[\[(.*?)\]\]', replace_standard_link, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Converted internal links in: {file_path}")

def copy_file(file_path: str, copy_to_path: str) -> Tuple[bool, str]:
    with open(file_path, "r") as f:
        content = f.read()
        if "#blog/publish" not in content:
            return False, None
    file_name_lower = os.path.basename(file_path).lower()

    # print(f"publish: {file_path}, ln: {line_number}")
    # copy that file to the publish notes directory
    copied_file_path = os.path.join(copy_to_path, file_name_lower)
    shutil.copy(file_path, copied_file_path)

    return True, copied_file_path

def find_image_and_copy(image_name: str, root_path: str, public_brain_image_path: str):
    text_files = glob.glob(root_path + "/**/" + image_name, recursive=True)
    for file in text_files:
        shutil.copy(file, public_brain_image_path)

def list_images_from_markdown(file_path: str):
    # search for images in markdown file
    file_content = open(file_path, "r").read()
    images = re.findall(regexp_md_images, file_content)
    if images:
        # print(f"-found images in {file_path}")
        for image in images:
            image_name = image[0]
            if image_name:
                find_image_and_copy(
                    image_name, second_brain_path, public_folder_path_copy
                )
    pass


def do_the_thing(second_brain_path: str, copy_to_path: str) -> None:
    for root, dirs, files in os.walk(second_brain_path):
        for file_path in [os.path.join(root, f) for f in files if f.endswith(".md")]:
            copied, copied_file_path = copy_file(file_path, copy_to_path)
            if not copied:
                continue

            process_file(file_path, copied_file_path)

def process_existing_content(content_dir: str) -> None:
    """
    Process all existing markdown files in the content directory.
    This is useful for updating links in already processed files.
    
    Parameters:
        content_dir (str): The path to the content directory.
    """
    print(f"Processing existing content in {content_dir}...")
    
    for file_name in os.listdir(secondbrain_public):
        if file_name.endswith(".md"):
            file_path = os.path.join(secondbrain_public, file_name)
            print(f"Processing existing file: {file_path}")
            
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace Hugo shortcode links with standard markdown links
            # This pattern handles [text]({< ref "path.md" >})
            content = re.sub(
                r'\[([^\]]+)\]\(\{\< ref "([^"]+)" \>\}\)', 
                lambda m: f'[{m.group(1)}](/{m.group(2).replace(".md", "")})', 
                content
            )
            
            # Also handle any remaining Obsidian-style links
            content = re.sub(
                r'\[\[(.*?)\|(.*?)\]\]', 
                lambda m: f'[{m.group(2)}](/{m.group(1).lower().replace(" ", "-")})', 
                content
            )
            
            content = re.sub(
                r'\[\[(.*?)\]\]', 
                lambda m: f'[{m.group(1)}](/{m.group(1).lower().replace(" ", "-")})', 
                content
            )
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Converted internal links in: {file_path}")
    
    print("Finished processing existing content.")

if __name__ == "__main__":
    # Process files from second brain
    do_the_thing(second_brain_path, public_folder_path_copy)
    
    # Process existing content files
    process_existing_content(public_folder_path_copy)
