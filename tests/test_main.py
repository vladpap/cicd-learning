from app.main import greet


def test_greet_default():
    assert greet() == "Hi, world!"


def test_greet_custom_name():
    assert greet("CI/CD") == "Hi, CI/CD!"


def test_greet_empty_name():
    assert greet("") == "Hi, !"