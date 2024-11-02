import pytest
from main import MainApp

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command and outputs the correct result."""
    inputs = iter(['divide 4 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as exit_info:
        app.load_plugins()
        app.start()
    
    assert exit_info.value.code == 0, "The app did not exit as expected"
    
    # Capture the output
    output, _ = capfd.readouterr()
    assert "2" in output, "The 'divide' command did not produce the expected output."

def test_divide_with_extra_parameters(capfd, monkeypatch):
    """Test that the 'divide' command handles extra parameters gracefully."""
    inputs = iter(['divide 4 2 9', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as exit_info:
        app.load_plugins()
        app.start()
    
    output, _ = capfd.readouterr()
    assert "Error: Requires exactly 2 parameters." in output, "Unexpected output for extra parameters in 'divide' command."

def test_divide_by_zero(capfd, monkeypatch):
    """Test that the 'divide' command correctly handles division by zero."""
    inputs = iter(['divide 4 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as exit_info:
        app.load_plugins()
        app.start()
    
    output, _ = capfd.readouterr()
    assert "Error: Division by zero is not allowed." in output, "Unexpected output when dividing by zero."

def test_divide_with_invalid_number(capfd, monkeypatch):
    """Test that the 'divide' command handles non-numeric input appropriately."""
    inputs = iter(['divide 4 a', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as exit_info:
        app.load_plugins()
        app.start()
    
    output, _ = capfd.readouterr()
    assert "Error: Parameters must be valid numbers." in output, "Unexpected output for invalid number input in 'divide' command."
