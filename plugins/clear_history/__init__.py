from commands import Command
import pandas as pd

class ClearHistoryCommand(Command):
    def execute(self, params = None):
        print("Clearing History")
        file_path = "csv/history.csv"

        clear_df = pd.DataFrame(columns = ["Command", "Parameter 1", "Parameter 2", "Result"])
        clear_df.to_csv(file_path, index = False)