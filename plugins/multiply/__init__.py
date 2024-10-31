from commands import Command

class MultiplyCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            try:
                a = int(params[0])  
                b = int(params[1])  
                print(a * b)  
            except ValueError:
                print("Error: Provide two valid numbers.")