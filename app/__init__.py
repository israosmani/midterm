import os
import sys
import pandas as pd
import pkgutil
import importlib
from plugins.add import AddCommand
from plugins.subtract import SubtractCommand
from plugins.multiply import MultiplyCommand
from plugins.divide import DivideCommand
from commands import Command
from commands import CommandHandler
from appLogger import AppLogger  # Changed import to use appLogger

class MainApp:
    def __init__(self):
        self.command_handler = CommandHandler()
        AppLogger.info("MainApp initialized.")

    def load_plugins(self):
        plugins_package = 'plugins'
        plugins_path = plugins_package.replace('.', '/')

        if not os.path.exists(plugins_path):
            AppLogger.warning(f"Plugins directory '{plugins_path}' not found.")
            return

        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                self.import_and_register_plugin(plugins_package, plugin_name)

    def import_and_register_plugin(self, plugins_package, plugin_name):
        try:
            plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
            self.register_commands_from_plugin(plugin_module, plugin_name)
        except ImportError as e:
            AppLogger.error(f"Error importing plugin {plugin_name}: {e}")

    def register_commands_from_plugin(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                command_instance = item()
                self.command_handler.register_command(plugin_name, command_instance)
                AppLogger.info(f"Registered command '{plugin_name}' from plugin '{plugin_name}'.")

    def append_to_history(self, cmd, num1, num2):
        file_path = 'data/history.csv'
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists(file_path):
            existing_data = pd.read_csv(file_path)
        else:
            existing_data = pd.DataFrame(columns=['command', 'num1', 'num2'])

        new_data = pd.DataFrame({
            'command': [cmd],
            'num1': [num1],
            'num2': [num2]
        })

        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_csv(file_path, index=False)
        AppLogger.info(f"Appended to history: {cmd} {num1} {num2}")

    def start(self):
        AppLogger.info("Starting application...")
        while True:
            user_input = input("Enter an input or command: ").strip().lower()

            if user_input == "exit":
                AppLogger.info("Exiting application.")
                sys.exit(0)

            self.execute_user_command(user_input)

    def execute_user_command(self, command):
        try:
            self.command_handler.execute_command(command)
        except Exception as e:
            AppLogger.error(f"Command execution failed: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    app = MainApp()
    app.load_plugins()
    app.start()
