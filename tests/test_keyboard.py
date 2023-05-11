from src.keyboard import Keyboard


def test_str():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"


def test_language_change():
    key = Keyboard('Dark Project KD87A', 9600, 5)
    key.change_lang()
    assert str(key.language) == "RU"


if __name__ == "__main__":
    test_language()
    test_str()
    test_language_change()
