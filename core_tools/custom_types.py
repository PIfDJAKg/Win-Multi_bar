class PCommand:
    def __init__(self, command, flag_list):
        self.command = command
        self.flag_list = flag_list


class PKeyWord:
    def __init__(self, word, data):
        self.word = word
        self.data = data


class PLink:
    def __init__(self, link):
        self.link = link