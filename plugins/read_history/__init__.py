from commands import Command
import pandas as pd

class ReadHistoryCommand(Command):
    def execute(self, params=None):
        print("Reading History")
        file_path = 'csv/history.csv'
        
        try:
            history_csv = pd.read_csv(file_path)
            if not history_csv.empty:
                for index, row in history_data.iterrows():
                    print(f"{row['Command']} {row['Parameter 1']} {row['Parameter 2']} -> Result: {row['Result']}")
            else:
                print("History is empty.")
        except FileNotFoundError:
            print("History not found.")
