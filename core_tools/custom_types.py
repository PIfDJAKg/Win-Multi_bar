class PCommand:
    def __init__(self, command, flags_dict):
        self.command = command
        self.flags_dict = flags_dict


class PKeyWord:
    def __init__(self, word, data):
        self.word = word
        self.data = data


class PLink:
    def __init__(self, link):
        self.link = link