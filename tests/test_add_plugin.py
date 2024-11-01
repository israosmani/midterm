import pytest
from app import MainApp
def test_app_add_command(capfd, monkeypatch):
    # Set up inputs 
    test_inputs = ['add 4 2', 'exit']
    monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))

    # Initialize  application
    app = MainApp()
    # Load plugins before starting the app
    app.load_plugins()

    with pytest.raises(SystemExit) as exit_info:
        app.start()

    assert exit_info.value.code == 0, "The application did not exit."

    output, error = capfd.readouterr()

    assert "6" in output, "The command did not give the expected output."
