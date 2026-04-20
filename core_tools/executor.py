import webbrowser
import os

from pygments.lexers.sql import googlesql_identifiers

from core_tools.custom_types import *


HOME_PATH = os.path.expanduser("~")


def execute(executable):
    if isinstance(executable, PCommand):
        if executable.command == "create":
            path = os.path.join(HOME_PATH, "Documents")
            name = "new_file"
            exp = ".txt"

            if "path" in executable.flags_dict:
                new_path = executable.flags_dict["path"]
                if new_path is not None:
                    path = new_path
            if "name" in executable.flags_dict:
                new_name = executable.flags_dict["name"]
                if new_name is not None:
                    name = new_name
            if "exp" in executable.flags_dict:
                new_exp = executable.flags_dict["exp"]
                if new_exp is not None:
                    exp = new_exp

            final_path = os.path.join(path, name + exp)

            open(final_path, "w").close()

    elif isinstance(executable, PKeyWord):
        if executable.word in ("g", "google", "search"):
            url = "https://www.google.com/search?q=" + executable.data
        elif executable.word == "spotify":
            if executable.data:
                url = "https://open.spotify.com/search/" + executable.data
            else:
                url = "https://open.spotify.com"
        elif executable.word in ("youtube", "yt"):
            if executable.data:
                url = "https://www.youtube.com/results?search_query=" +executable.data
            else:
                url = "https://www.youtube.com/"
        elif executable.word == "pinterest":
            url = "https://www.pinterest.com/search/pins/?q=" + executable.data
        elif executable.word == "github":
            if executable.data:
                url = "https://github.com/search?q=" + executable.data
            else:
                url = "https://github.com/search?q=somethink"
        elif executable.word == "pypi":
            if executable.data:
                url = "https://pypi.org/search/?q=" + executable.data
            else:
                url = "https://pypi.org/"
        elif executable.word == "stackoverflow":
            if executable.data:
                url = "https://stackoverflow.com/search?q=" + executable.data
            else:
                url = "https://stackoverflow.com/"
        elif executable.word in ("wiki", "wikipedia"):
            if executable.data:
                url = "https://ru.wikipedia.org/w/index.php?&search=" + executable.data
            else:
                url = "https://ru.wikipedia.org/"
        elif executable.word == "reddit":
            if executable.data:
                url = "https://www.reddit.com/search/?q=" + executable.data
            else:
                url = "https://www.reddit.com/"
        else:
            url = "https://example.com/"

        webbrowser.open_new_tab(url)
    elif isinstance(executable, PLink):
        webbrowser.open_new_tab(executable.link)