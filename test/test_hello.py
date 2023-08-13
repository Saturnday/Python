from hello_unit import say_hello

def test_say_hello():
    assert say_hello("Name")=="Hello, Name"