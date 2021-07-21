#!/usr/bin/env python3

import re
import markdown
from markdown.extensions.toc import TocExtension
from bin.custom_blocks import markdown_inset_text

# basic markdown setup
md = markdown.Markdown(
    extensions=[TocExtension(toc_depth="3"), "tables", "customblocks"],
    extension_configs={
        "customblocks": {
            "generators": {
                # by direct symbol reference
                "inset-text": markdown_inset_text,
            }
        },
    },
)


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

    html = html.replace("<table>", '<table class="govuk-table">')
    html = html.replace("<thead>", '<thead class="govuk-table__head">')
    html = html.replace("<tbody>", '<tbody class="govuk-table__body">')
    html = html.replace("<tr>", '<tr class="govuk-table__row">')
    html = html.replace("<td", '<td class="govuk-table__cell"')
    html = html.replace("<th>", '<th class="govuk-table__header">')

    html = re.sub("<th(>|\s)", '<th class="govuk-table__header" ', html)

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
