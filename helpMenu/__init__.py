import sys

import markdown
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTextBrowser

def get_markdown(lang:str) -> str:
    print("start")
    file_path = ""
    match lang.lower():
        case "ru":
            file_path = "README_RUS.md"
        case "eng":
            file_path = "README.md"
        case _:
            file_path = "README_RUS.md"

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def convert_md_to_html(md:str) -> str:
    html_body = markdown.markdown(md)
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 20px;
                    color: #333;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            {html_body}
        </body>
        </html>
        """
    return html

class HelpMenu(QtWidgets.QWidget):
    def __init__(self, lang:str="eng"):
        super().__init__()
        print("help_menu_create")
        self.lang = lang
        print("getting_html")
        self.html_text = convert_md_to_html(get_markdown(self.lang))

        self.setFixedSize(800, 800)
        self.setWindowTitle("Help Menu")

        self.layout = QtWidgets.QHBoxLayout(self)

        self.view = QTextBrowser()
        self.view.setHtml(self.html_text)

        self.layout.addWidget(self.view)
        print("complete")

def view_help_menu(lang:str):
    print("1")
    app = QtWidgets.QApplication(sys.argv)
    print("2")
    hm = HelpMenu(lang)
    hm.show()
    print("3")
    sys.exit(app.exec())