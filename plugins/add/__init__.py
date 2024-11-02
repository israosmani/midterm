from commands import Command
from appLogger import AppLogger  #importing for loggings

class AddCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            try:
                a, b = (int(param) for param in params)  
                result = a + b
                print(result) 
                return result
            except ValueError:
                print("Error: Parameters must be integers.")
                AppLogger.log("Addition failed due to invalid input")
            
        else:
            print("Error: 'add' command requires exactly 2 parameters.")
            AppLogger.log("Addition failed due to incorrect number of parameters")
