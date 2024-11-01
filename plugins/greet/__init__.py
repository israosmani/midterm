from commands import Command

class GreetCommand(Command):
    def execute(self, greeting="Hello", name="User"):
        message = f"{greeting}, {name}!"
        print(message)
