from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_str():
    assert str(kb) == "Dark Project KD87A"


test_str()


def test_language():
    assert str(kb.language) == "EN"


test_language()


def test_language_change():
    key = Keyboard('Dark Project KD87A', 9600, 5)
    key.change_lang()
    assert str(key.language) == "RU"


test_language_change()
