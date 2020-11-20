#!/usr/bin/env python3

import os
import sys
import json

from bin.jinja_setup import setup_jinja, render

env = setup_jinja()
env.globals["staticPath"] = "https://digital-land.github.io"
# get templates
index_template = env.get_template("index.html")


def generate_guidance_pages():
    with open("config/pages.json") as file:
        data = json.load(file)

    render("index.html", index_template, pages=data["pages"])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        env.globals["urlPath"] = ""

    generate_guidance_pages()
