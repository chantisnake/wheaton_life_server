from bs4 import NavigableString


def strip_html(src):
    striped_text = src.findAll(text=lambda text: isinstance(text, NavigableString))
    return "".join(striped_text)