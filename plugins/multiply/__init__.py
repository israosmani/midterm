from commands import Command
from appLogger import AppLogger

class MultiplyCommand(Command):
    def execute(self, params):
        if len(params) != 2:
            print("Error: The 'multiply' command requires exactly 2 parameters.")
            AppLogger.log("Multiplication failed due to incorrect parameter count")
            return None

        try:
            factor1, factor2 = int(params[0]), int(params[1])  # Convert parameters to integers
            product = factor1 * factor2
            print(product)  # Output the result
            return product
        except ValueError:
            print("Error: Both parameters must be valid numbers.")
            AppLogger.log("Multiplication failed due to invalid input type")
            return None
