import pytest
from main import MainApp

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command and outputs the correct result."""
    
    inputs = iter(['add 3 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as exit_info:
        app.load_plugins()
        app.start()
    
    assert exit_info.value.code == 0, "Expected the app to exit with code 0"

    output, _ = capfd.readouterr()

    # Assert that the output contains the expected result
    assert "5" in output, "The output did not include the expected result of the 'add' command."
