# Updated test code
from pathlib import Path
import pytest
from main import MainApp

def test_menu_command_display(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    """Test that the menu command displays available commands correctly and exits as expected."""

    # Set up 'menu' command followed by 'exit'
    simulated_inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(simulated_inputs))

    app = MainApp()
    
    with pytest.raises(SystemExit) as exit_info:
        app.load_plugins()
        app.start()
    
    assert exit_info.value.code == 0, "The application did not exit as expected."

    # Capture output
    output_capture = capfd.readouterr()
    
    # Assert should include the command list
    expected_output = "Commands: "  
    assert expected_output in output_capture.out, "Expected command list header not found."
    assert "add" in output_capture.out, "Expected 'add' command not found in output."
    assert "subtract" in output_capture.out, "Expected 'subtract' command not found in output."
    assert "multiply" in output_capture.out, "Expected 'multiply' command not found in output."
