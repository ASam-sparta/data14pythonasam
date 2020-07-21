from input_trial import take_input
from io import StringIO

def test_take_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("Hello"))
    assert take_input() == "Hello"