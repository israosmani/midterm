import pytest
from main import MainApp
import pandas as pd

def create_mock_history_file(tmp_path):
    history_file = tmp_path / "history.csv"
    command_data = {"command": ["add 1 2", "multiply 3 4", "divide 10 2"]}
    history_df = pd.DataFrame(command_data)
    history_df.to_csv(history_file, index=False)
    return history_file

def test_read_history_command_without_params(capfd, monkeypatch, tmp_path):
    
    history_file_path = create_mock_history_file(tmp_path)

    user_inputs = iter(['read_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))

    app = MainApp()
    app.history_file = str(history_file_path)  

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    output_capture = capfd.readouterr()
    assert "History loaded successfully. Total entries:" in output_capture.out, "Expected history load message not found."

def test_read_history_with_extra_params(capfd, monkeypatch, tmp_path):
    
    history_file_path = create_mock_history_file(tmp_path)
    #read history
    user_inputs = iter(['read_history extra_param', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))

    # set the history file
    app = MainApp()
    app.history_file = str(history_file_path)

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    # verify the output
    output_capture = capfd.readouterr()
    assert "Error: Command does not take any parameters." in output_capture.out, "Expected parameter error message not found."
