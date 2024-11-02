import pytest
from main import MainApp

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL processes the 'subtract' command and returns the correct result."""
    inputs = iter(['subtract 2 1', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as exit_context:
        app.load_plugins()
        app.start()
    
    assert exit_context.value.code == 0, "The application did not exit as expected"
    
    # Capture the output 
    output, _ = capfd.readouterr()
    
    assert "1" in output, "The output for the 'subtract' command was not as expected."
