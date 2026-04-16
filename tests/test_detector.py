from core_tools.parser import get_n_word

def test_word():
    assert get_n_word("one two three four Mike minecraft", 5) == "Mike"