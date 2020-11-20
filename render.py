#!/usr/bin/env python3

import os
import json

from bin.jinja_setup import env, render

env.globals["staticPath"] = "https://digital-land.github.io"
# get templates
index_template = env.get_template("index.html")

with open("config/pages.json") as file:
    data = json.load(file)

render("index.html", index_template, pages=data['pages'])
