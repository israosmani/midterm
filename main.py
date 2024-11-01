import sys
import csv
import pandas as pd  
import os
import pkgutil
import importlib
from commands import Command
from plugins.add import AddCommand
from plugins.subtract import SubtractCommand
from plugins.multiply import MultiplyCommand
from plugins.divide import DivideCommand
from plugins.clear_history import ClearHistoryCommand
from plugins.read_history import ReadHistoryCommand

class Main:
    def __init__(self):
        self.command_list = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
            "clear_history": ClearHistoryCommand(),
            "read_history": ReadHistoryCommand()
        }

    def load_plugins(self):
        plugins_package = 'plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            print(f"Plugins directory '{plugins_path}' not found.")
            return

        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    print(f"Error importing plugin {plugin_name}: {e}")  

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_list[plugin_name] = item()
    
    def appendHistory(self, cmd, num1, num2):
        file_path = 'csv/history.csv'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if not os.path.isfile(file_path):
            pd.DataFrame(columns=['command', 'num1', 'num2']).to_csv(file_path, index=False)

        existing_csv = pd.read_csv(file_path)
        new_data = pd.DataFrame({
            'command': [cmd],
            'num1': [num1],
            'num2': [num2]    
        })
        updated_csv = pd.concat([existing_csv, new_data], ignore_index=True)
        updated_csv.to_csv(file_path, index=False)
    
    def clearHistory(self): 
        file_path = 'csv/history.csv'
        if os.path.isfile(file_path):
            open(file_path, 'w').close()
    
    def readHistory(self): 
        file_path = 'csv/history.csv'
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            print(df)
        else:
            print("History not found.")

    def repl(self):
        while True:
            val = input("Enter input: ")
            if val.lower() == "exit":
                print("Exiting REPL.")
                break

            if val.lower() == "clear":
                self.clearHistory()
                print("History cleared.")
                continue 
            elif val.lower() == "read":
                self.readHistory()
                continue 

            user_input = val.split()
            if len(user_input) < 3:
                print("Please provide a command followed by two numbers.")
                continue

            cmd, num1, num2 = user_input[0], user_input[1], user_input[2]

            try:
                if cmd in self.command_list:
                    command = self.command_list[cmd]
                    command.execute(params=(num1, num2))
                    self.appendHistory(cmd, num1, num2)  
                else:
                    print("Invalid command")
            except Exception as e:
                print(f"Execution failed: {e}")

if __name__ == "__main__":
    app = Main()
    app.load_plugins()
    app.repl()
