#!/usr/bin/env python3

from bin.utils import basic_MD


def parse(s, parser):
    return parser.convert(s)


def markdown_inset_text(ctx):
    return f'<div class="govuk-inset-text">{parse(ctx.content, basic_MD)}</div>'
