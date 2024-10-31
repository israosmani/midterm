import sys
from plugins.add import AddCommand
from plugins.subtract import SubtractCommand
from plugins.multiply import MultiplyCommand
from plugins.divide import DivideCommand

def repl():
    command_list = {
        "add": AddCommand(),
        "subtract": SubtractCommand(),
        "multiply": MultiplyCommand(),
        "divide": DivideCommand()
    }

    while True:
        val = input("Enter input (command, num1, num2): ")
        if val.lower() == "exit":
            print("Exiting REPL.")
            break

        user_input = val.split()
        if len(user_input) < 3:
            print("Please provide a command followed by two numbers.")
            continue

        cmd, num1, num2 = user_input[0], user_input[1], user_input[2]

        try:
            if cmd in command_list:
                command = command_list[cmd]
                command.execute(params=(num1, num2))
            else:
                print("Invalid command")
        except Exception as e:
            print(f"Execution failed: {e}")

if __name__ == "__main__":
    repl()
