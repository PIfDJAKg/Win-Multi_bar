import webbrowser
from os.path import join
import subprocess

from core_tools.custom_types import *


def execute(executable):
    if isinstance(executable, PCommand):
        pass
    elif isinstance(executable, PKeyWord):
        if executable.word in ("g", "google", "search"):
            url = f"https://www.google.com/search?q={executable.data}"
            webbrowser.open_new_tab(url)
        elif executable.word == "pinterest":
            url = f"https://www.pinterest.com/search/pins/?q={executable.data}"
            webbrowser.open_new_tab(url)
    elif isinstance(executable, PLink):
        webbrowser.open_new_tab(executable.link)