#!/usr/bin/env python3

import os
import sys
import json

from bin.jinja_setup import setup_jinja, render
from bin.markdown import markdown_compile, get_contents_section

from frontmatter import Frontmatter

env = setup_jinja()
env.globals["staticPath"] = "https://digital-land.github.io"
# get templates
index_template = env.get_template("index.html")
guidance_template = env.get_template("guidance.html")


def markdown_files_only(files, file_ext=".md"):
    return [f for f in files if f.endswith(file_ext)]


def generate_guidance_idx_page():
    with open("config/pages.json") as file:
        data = json.load(file)

    render("index.html", index_template, pages=data["pages"])


def generate_guidance_page(root):
    page_content = Frontmatter.read_file(f"{root}/index.md")
    html = markdown_compile(page_content["body"])

    # strip 'content/'
    dist = root.replace("content/", "")

    content = {"main": html}
    if page_content["attributes"].get("hasContents"):
        content["contents"] = get_contents_section()
    render(
        f"{dist}/index.html",
        guidance_template,
        content=content,
        fm=page_content["attributes"],
    )


def loop_over_directory(target_dir):
    for root, dir_names, file_names in os.walk(target_dir):
        for d in dir_names:
            # will need to do the same again
            child_dir = f"{root}/{d}"
            pass
        for f in file_names:
            if f == "index.md":
                generate_guidance_page(root)


def generate_guidance_pages():
    generate_guidance_idx_page()

    loop_over_directory("content/")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    generate_guidance_pages()
