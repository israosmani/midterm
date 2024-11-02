from commands import Command
from appLogger import AppLogger

class DivideCommand(Command):
    def execute(self, params):
        if len(params) != 2:
            print("Error: Requires exactly 2 parameters.")
            AppLogger.log("Division failed due to incorrect parameter count")
            return None

        try:
            numerator, denominator = int(params[0]), int(params[1])  # Convert parameters to integers
            if denominator == 0:
                print("Error: Division by zero is not allowed.")
                AppLogger.log("Division failed ")
                return None
            
            result = numerator / denominator
            print(result)  # Output the result
            return result
        except ValueError:
            print("Error: Parameters must be valid numbers.")
            AppLogger.log("Division failed ")
            return None
