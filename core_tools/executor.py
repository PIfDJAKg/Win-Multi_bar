import webbrowser
import os
from helpMenu import view_help_menu

from core_tools.custom_types import *


HOME_PATH = os.path.expanduser("~")


SEARCH_KEYWORDS = {
    "google": (
        ["g, google, search"], "https://www.google.com/", "search?q="
    ),
    "spotify": (
        ["spotify", "spfy"], "https://open.spotify.com/", "search/"
    ),
    "youtube": (
        ["youtube", "yt"], "https://www.youtube.com/", "results?search_query="
    ),
    "pinterest": (
        ["pinterest", "pin"], "https://www.pinterest.com/", "search/pins/?q="
    ),
    "github": (
        ["github", "git", "ghub"], "https://github.com/", "search?q="
    ),
    "pypi": (
        ["pypi"], "https://pypi.org/", "search/?q="
    ),
    "stackoverflow": (
        ["stackoverflow", "sflow"], "https://stackoverflow.com/", "search?q="
    ),
    "wikipedia": (
        ["wikipedia", "wiki"], "https://wikipedia.org/", "w/index.php?&search="
    ),
    "ruwikipedia": (
        ["rwikipedia", "rwiki", "ruwikipedia", "ruwiki", "википедия", "вики"], "https://ru.wikipedia.org/", "w/index.php?&search="
    ),
    "reddit": (
        ["reddit", "r"], "https://www.reddit.com/", "search/?q="
    ),
}

def _execute_search_keyword(keyword:PKeyWord) -> None:
    word = keyword.word
    data = keyword.data
    for KEYWORD in SEARCH_KEYWORDS:
        if word in SEARCH_KEYWORDS[KEYWORD][0]:
            url = SEARCH_KEYWORDS[KEYWORD][1]
            if data:
                url += SEARCH_KEYWORDS[KEYWORD][2] + data
            webbrowser.open_new_tab(url)
            break

def execute(executable):
    if isinstance(executable, PCommand):
        if executable.command == "create":
            path = os.path.join(HOME_PATH, "Documents")
            name = "new_file"
            ext = ".txt"

            if "path" in executable.flags_dict:
                new_path = executable.flags_dict["path"]
                if new_path is not None:
                    path = new_path
            if "name" in executable.flags_dict:
                new_name = executable.flags_dict["name"]
                if new_name is not None:
                    name = new_name
            if "ext" in executable.flags_dict:
                new_ext = executable.flags_dict["ext"]
                if new_ext is not None:
                    ext = new_ext

            final_path = os.path.join(path, name + ext)

            open(final_path, "w").close()
        if executable.command == "help":
            print("getting_lang")
            lang = "eng"
            if "lang" in executable.flags_dict:
                lang = executable.flags_dict["lang"].lower()

            print("view")
            view_help_menu(lang)


    elif isinstance(executable, PKeyWord):
        _execute_search_keyword(executable)
    elif isinstance(executable, PLink):
        webbrowser.open_new_tab(executable.link)