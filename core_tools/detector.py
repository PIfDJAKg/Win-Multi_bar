import core_tools.parser as parser
from core_tools.custom_types import PLink

keywords: tuple = (
    'yt',
    'cmd',
    'music',
    'open',
    'search',
    'g',
    'google',
    'pinterest',
    'create',
)


def get_first_word(data:str) -> str:
    return data.split()[0] if data else ""


def detect(data):
    if ' ' in data:  # check on spaces
        if data.startswith(keywords):  # check on keywords
            return parser.parse_keyword(data)
        elif get_first_word(data)[0] == "!":
            return parser.parse_command(data)
        return None
    else:
        if data.startswith(("https://", "http://", "www.")):  # check on link
            return PLink(data)
        return None