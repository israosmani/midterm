import pytest
from main import MainApp

def test_greet_command_output(capfd, monkeypatch):
    user_inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))

    app_instance = MainApp()
    with pytest.raises(SystemExit) as exit_info:
        app_instance.load_plugins()
        app_instance.start()

    assert exit_info.value.code == 0, "The application did not exit."

    captured_output, _ = capfd.readouterr()

    assert "Hello, User!" in captured_output, "The output is not as expected."
