from commands import Command

class SubtractCommand(Command):
    def execute(self, params):
        if len(params) == 2:
            a = int(params[0])  
            b = int(params[1])  
            print(a - b)
