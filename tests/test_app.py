import pytest
from main import MainApp


def test_app_start_exit_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = MainApp()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    inputs = iter(['abc', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()

    captured = capfd.readouterr()
    assert "No such command: abc" in captured.out