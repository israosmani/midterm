import sys
import Command from 

def repl():
    while True:
        val = input("Enter input: ")
        userInput = val.split()  
        cmd, num1, num2 = userInput[0], userInput[1], userInput[2]

        commandList = {
            "add": AddCommand, 
            "subtract": SubtractCommand, 
            "multiply": MultiplyCommand, 
            "divide": DivideCommand 
        }


        try:
            commandClass = commandList[cmd]
            commandClass.execute(self, params=(num1, num2))
        except KeyError:
            print("Invalid Command")
        except Exception:
            print("Execution failed")

if __name__ == "__main__":
    repl()