from core_tools.custom_types import PCommand, PKeyWord


def parse_flags(data:str) -> dict:
    words = data.split()
    words_count = len(words)

    if words_count == 0:
        return {}

    flags = {}
    i = 0
    word = words[i]
    while i < words_count:
        if word.startswith("--"):
            if i < words_count - 1:
                value = words[i + 1]

                if value.startswith("--"):
                    value = None
                else:
                    i += 1
            else:
                value = None

            flags[word[2:]] = value
            i += 1
            if i < words_count:
                word = words[i]
        else: return None
    return flags


def get_n_word(data:str, i:int) -> str:
    words = data.split()
    if 0 < i <= len(words):
        return words[i - 1]
    return ""


def parse_command(data:str) -> PCommand:
    command_name = get_n_word(data, 1)[1:]
    name_lenght = len(command_name) + 2 # 1 - это удаленный восклицательный знак "!" и пробел
    flags_dict = parse_flags(data[name_lenght:])

    print(f"Command name: {command_name}, flags: {flags_dict}")

    return PCommand(command_name, flags_dict)


def parse_keyword(data:str) -> PKeyWord:
    word = get_n_word(data, 1)
    word_len = len(word)
    data = data[word_len:]

    return PKeyWord(word, data)