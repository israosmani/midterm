import pytest
from main import MainApp 

def test_app_greet_command(capfd, monkeypatch):
    
    # Define the inputs 
    inputs = ['greet', 'exit']
    
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    app = MainApp()
    app.load_plugins()  # Plugins loaded

    try:
        app.start()
    except SystemExit as e:
        assert e.code == 0, "The app did not exit as expected."

    out, err = capfd.readouterr()
    
    assert "Hello User" in out, "The command did not provide expected output."
