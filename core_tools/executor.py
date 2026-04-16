import webbrowser
import os

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
            url = f"https://www.google.com/search?q={executable.data}"
            webbrowser.open_new_tab(url)
        elif executable.word == "pinterest":
            url = f"https://www.pinterest.com/search/pins/?q={executable.data}"
            webbrowser.open_new_tab(url)
    elif isinstance(executable, PLink):
        webbrowser.open_new_tab(executable.link)