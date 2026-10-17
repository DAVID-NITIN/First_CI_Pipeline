import importlib

largest_word = importlib.import_module("21_largest_word").largest_word


def test_largest_word_basic():
    assert largest_word("Python is awesome") == "awesome"


def test_largest_word_single_word():
    assert largest_word("Hello") == "Hello"


def test_largest_word_empty_sentence():
    assert largest_word("") == ""


def test_largest_word_multiple_spaces():
    assert largest_word("I love programming") == "programming"