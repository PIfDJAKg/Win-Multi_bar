import core_tools.parser as parser
from core_tools.custom_types import PLink

keywords: tuple = (
    'yt', # +
    'youtube', # +
    'stackoverflow', # +
    'wikipedia', # +
    'wiki', # +
    'reddit', # +
    'pypi', # +
    'github', # +
    'spotify', # +
    'search', # +
    'g', # +
    'google', # +
    'pinterest', # +
)


def get_first_word(data:str) -> str:
    return data.split()[0] if data else ""


def detect(data):
    if ' ' not in data:  # check on spaces:
        if data.startswith(("https://", "http://", "www.")):  # check on link
            return PLink(data)

    if data.startswith(keywords) or data in keywords:  # check on keywords
        return parser.parse_keyword(data)
    elif data[0] == "!":
        return parser.parse_command(data)
    return None