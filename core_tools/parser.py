from core_tools.custom_types import PCommand, PKeyWord


def get_n_word(data:str, i:int) -> str:
    words = data.split()
    if 0 < i <= len(words):
        return words[i - 1]
    return ""


def parse_command(data):
    n = 1
    command_name = get_n_word(data, n)[1:]

    flag_list = []
    n += 1
    word = get_n_word(data, n)
    while word.startswith("--"):
        flag_list.append(word[2:])

    return PCommand(command_name, flag_list)


def parse_keyword(data):
    word = get_n_word(data, 1)
    word_len = len(word)
    data = data[word_len:]

    return PKeyWord(word, data)