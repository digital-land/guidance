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


def generate_guidance_pages():
    with open("config/pages.json") as file:
        data = json.load(file)

    render("index.html", index_template, pages=data["pages"])

    guidance_dir = "content/"
    sections = os.listdir(guidance_dir)

    print(sections)
    for section in sections:
        page_content = Frontmatter.read_file(f"{guidance_dir}{section}/index.md")
        html = markdown_compile(page_content["body"])

        content = {"main": html}
        if page_content["attributes"]["hasContents"]:
            content["contents"] = get_contents_section()
        render(
            f"{section}/index.html",
            guidance_template,
            content=content,
            fm=page_content["attributes"],
        )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    generate_guidance_pages()
