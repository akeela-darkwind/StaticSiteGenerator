import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    # Walk through all files in content directory
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                # Construct the input path
                input_path = os.path.join(root, file)
                
                # Determine the output path in the public directory
                rel_path = os.path.relpath(root, dir_path_content)
                output_dir = os.path.join(dir_path_public, rel_path)
                
                # Create output directory if it doesn't exist
                os.makedirs(output_dir, exist_ok=True)
                
                # Replace .md with .html for the output file
                output_filename = file.replace('.md', '.html')
                output_path = os.path.join(output_dir, output_filename)
                
                print(f" * {input_path} {template_path} -> {output_path}")
                generate_page(input_path, template_path, output_path)

main()
