from commands import Command

class DivideCommand(Command):
    def execute(self, params):
        if len(params) != 2:
            print("Error: Need two arguments.")
            return None
        
        try:
            a = int(params[0])  
            b = int(params[1])              
            if b == 0:
                print("Error: Cannot divide by zero.")
                return None
            
            result = a / b  
            print(result)  
            return result
        
        except ValueError:
            print("Error: Provide two valid numbers.")
            return None