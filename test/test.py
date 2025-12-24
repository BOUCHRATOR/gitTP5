from tp5 import greet
def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Bonjour, Alice!\n"
