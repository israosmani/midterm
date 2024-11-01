from abc import ABC, abstractmethod
import pandas as pd

class Command(ABC):
    @abstractmethod
    def execute(self, params):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def append_to_history(self, full_command: str):
        file_path = 'csv/history.csv'
        
        try:
            existing_data = pd.read_csv(file_path)
        except FileNotFoundError:
            existing_data = pd.DataFrame(columns=['command'])

        new_data = pd.DataFrame({
            'command': [full_command],
        })

        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_csv(file_path, index=False)

    def execute_command(self, full_command: str):
        command_parts = full_command.split()
        command_name = command_parts[0]
        params = command_parts[1:]  

        if command_name in self.commands:
            self.commands[command_name].execute(params)
            self.append_to_history(full_command)
        else:
            print(f"No such command: {command_name}")

