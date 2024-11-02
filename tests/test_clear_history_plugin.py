import pytest
from main import MainApp
import pandas as pd

def create_mock_history_file(tmp_path):
    history_file_path = tmp_path / "history.csv"
    commands = pd.DataFrame({"command": ["add 4 2", "multiply 3 6", "divide 15 5"]})
    commands.to_csv(history_file_path, index=False)
    return history_file_path

def test_clear_history_functionality(capfd, monkeypatch, tmp_path):

    history_file = create_mock_history_file(tmp_path)

    user_inputs = iter(['clear_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))

    app = MainApp()
    app.history_file = str(history_file) 

    with pytest.raises(SystemExit):
        app.load_plugins()
        app.start()

    output_capture = capfd.readouterr()
    
    #assertions
    assert "History cleared." in output_capture.out, "Expected success message was not found."

    
