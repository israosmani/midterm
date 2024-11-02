from commands import Command

class GreetCommand(Command):
    def execute(self, params):
        print("Hello, User!")