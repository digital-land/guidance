#!/usr/bin/env python3

import markdown
from markdown.extensions.toc import TocExtension

basic_MD = markdown.Markdown(extensions=[TocExtension(toc_depth="2"), "tables"])
