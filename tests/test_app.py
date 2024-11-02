import pytest
from main import MainApp

def test_exit_command_execution(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app_instance = MainApp()
    with pytest.raises(SystemExit):
        app_instance.start()

def test_unknown_command_execution(capfd, monkeypatch):
    user_inputs = iter(['abc', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))

    app_instance = MainApp()
    
    with pytest.raises(SystemExit):
        app_instance.start()

    captured_output = capfd.readouterr()
    assert "No such command: abc" in captured_output.out, f"Captured output: {captured_output.out}"

def test_add_command_with_extra_params(capfd, monkeypatch):
    """Verify that the REPL responds appropriately when the 'add' command is given too many parameters."""
    user_inputs = iter(['add 4 2 9', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))

    app_instance = MainApp()
    with pytest.raises(SystemExit):
        app_instance.load_plugins()
        app_instance.start()
    
    output, _ = capfd.readouterr()

    assert "Error: 'add' command requires exactly 2 parameters." in output, "The 'add' command error message is not as expected."
