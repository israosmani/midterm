from commands import Command
from appLogger import AppLogger

class SubtractCommand(Command):
    def execute(self, params):
        if len(params) != 2:
            print("Error: The 'subtract' command requires exactly 2 parameters.")
            AppLogger.log("Subtraction failed due to incorrect parameter count")
            return None

        try:
            minuend, subtrahend = int(params[0]), int(params[1])  # Convert parameters to integers
            difference = minuend - subtrahend
            print(difference)  # Output the result
            return difference
        except ValueError:
            print("Error: Both parameters must be valid numbers.")
            AppLogger.log("Subtraction failed due to invalid input type")
            return None
