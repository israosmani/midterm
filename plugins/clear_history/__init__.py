from commands import Command
import pandas as pd
import os

class ClearHistoryCommand(Command):
    def execute(self, params):
        if len(params) > 0:
            print("ERROR: Cannot accept parameters.")
            return

        history_file = 'csv/history.csv'  # Make sure this points to the correct file
        headers = ['command']
        pd.DataFrame(columns=headers).to_csv(history_file, index=False)
        print("History cleared.")  # This should match the expected assertion

