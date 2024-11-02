from commands import Command
import pandas as pd
import os

class ReadHistoryCommand(Command):
    def execute(self, params):
        if len(params) > 0:
            print("Error: Command does not take any parameters.")
            return

        history_file = 'csv/history.csv'
        
        history_df = pd.read_csv(history_file)
        print("History loaded successfully. Total entries:", len(history_df))
