from hello_unit import say_hello

def test_say_hello():
    assert say_hello("mike") == "Hello, mike"
    assert say_hello("") == "Hello, world"