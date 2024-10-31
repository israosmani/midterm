from commands import Command

class GreetCommand(Command):
    def execute(self):
        print("Hello, World!")