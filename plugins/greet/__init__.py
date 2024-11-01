from commands import Command

class GreetCommand(Command):
    def execute(self, greeting= "Hello, World!"):
        print(greeting)