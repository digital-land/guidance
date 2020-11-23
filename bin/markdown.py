#!/usr/bin/env python3

import markdown
from markdown.extensions.toc import TocExtension

# basic markdown setup
md = markdown.Markdown(extensions=[TocExtension(toc_depth="2")])


def apply_our_classes(html):
    html = html.replace("<p>", '<p class="govuk-body">')
    html = html.replace("<h1", '<h1 class="govuk-heading-xl" ')
    html = html.replace("<h2", '<h2 class="govuk-heading-l" ')
    html = html.replace("<h3", '<h3 class="govuk-heading-m" ')
    html = html.replace("<h4", '<h4 class="govuk-heading-s" ')
    html = html.replace("<ul>", '<ul class="govuk-list govuk-list--bullet">')
    html = html.replace("<ol>", '<ol class="govuk-list govuk-list--number">')
    html = html.replace("<pre>", '<pre class="hljs-container">')
    html = html.replace("<code>", '<code class="dl-code">')
    return html


def markdown_compile(s):
    html = md.convert(s)
    html = apply_our_classes(html)
    return html


def get_contents_section():
    contents = md.toc
    contents = contents.replace(
        '<div class="toc">',
        '<div class="govuk-grid-column-one-third contents-section">\n<p>Contents</p>',
    )
    return contents
