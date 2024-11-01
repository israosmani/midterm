import pytest
from main import MainApp
from unittest.mock import patch, MagicMock
from appLogger import AppLogger  # Updated to import for appLogger

class TestMainApp:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.app = MainApp()

    @patch('os.path.exists')
    @patch('pkgutil.iter_modules')
    @patch('importlib.import_module')
    def test_load_plugins(self, mock_import_module, mock_iter_modules, mock_path_exists):
        mock_path_exists.return_value = True
        mock_iter_modules.return_value = [(None, 'add', True), (None, 'subtract', True)]
        
        mock_plugin_module = MagicMock()
        mock_import_module.return_value = mock_plugin_module
        
        mock_command_class = MagicMock()
        mock_command_class.return_value = MagicMock()
        mock_plugin_module.AddCommand = mock_command_class
        mock_plugin_module.SubtractCommand = mock_command_class

        self.app.load_plugins()

        assert self.app.command_handler.commands == {'add': mock_command_class.return_value,
                                                     'subtract': mock_command_class.return_value}
        AppLogger.info("Plugins loaded successfully.")

    @patch('pandas.read_csv')
    @patch('pandas.DataFrame.to_csv')
    def test_append_to_history(self, mock_to_csv, mock_read_csv):
        """Test appending to history."""
        mock_read_csv.return_value = pd.DataFrame(columns=['command', 'num1', 'num2'])
        
        self.app.append_to_history('add 4 2', 4, 2)
        
        mock_to_csv.assert_called_once()
        assert mock_to_csv.call_args[0][0] == 'csv/history.csv'

    @patch('builtins.input', side_effect=['add 4 2', 'exit'])
    @patch('main.Logger.log')
    @patch('main.MainApp.command_handler.execute_command')
    def test_start_method(self, mock_execute_command, mock_log, mock_input):
        """Test the command input loop."""
        mock_execute_command.return_value = None

        with patch('sys.exit') as mock_exit:
            self.app.start()
            mock_exit.assert_called_once_with(0)  

    @patch('main.Logger.log')
    @patch('main.MainApp.command_handler.execute_command')
    def test_start_method_execute_command_failure(self, mock_execute_command, mock_log):
        """Test handling command execution failure."""
        mock_execute_command.side_effect = Exception("Command execution error")

        with patch('builtins.input', side_effect=['unknown_command', 'exit']):
            with patch('sys.exit') as mock_exit:
                self.app.start()
                mock_log.assert_called_with("Execute command failed with error Command execution error")
                mock_exit.assert_called_once_with(0)

if __name__ == "__main__":
    pytest.main()
