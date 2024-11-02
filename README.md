**Link to my repository**
https://drive.google.com/file/d/1BU2r9VzvHThps6bnsC_3_XpyRjqcZkD4/view?usp=sharing 

Setup Instructions
Clone the repository: 
git clone <repository_url>
cd <repository_name>

Create a Virtual Environment:
python3 -m venv env
source env/bin/activate  # For Linux
env\Scripts\activate     # For Windows

Install Dependencies: Ensure that required packages (e.g., pandas) are specified in requirements.txt, then run:
pip install -r requirements.txt

Run the Application: Start the main application by running
python app/main.py

**Usage Examples**
**Basic Arithmetic Operations:**

Add: add 5 3 - Outputs the sum of 5 and 3 which is 8.

Subtract: subtract 10 4 - Outputs the result of 10 minus 4 which is 6.

Multiply: multiply 7 8 - Outputs the product of 7 and 8 which is 54.

Divide: divide 20 5 - Outputs the result of 20 divided by 5 which is 4.

Other Commands:

Greet: greet - Outputs a friendly greeting, in this case, "Hello, User!"

Menu: menu - Lists all available commands.

Clear History: clear_history - Clears the command usage history.

**Architectural Overview**

This application follows a modular architecture with a plugin-based design, enabling extensibility and separation of concerns. Key architectural decisions include:

**Command Handler:** The CommandHandler class in commands/__init__.py manages the registration and execution of commands. Each command implements the abstract Command class, enforcing a consistent interface.

**Plugin-Based Design:** Commands are implemented as individual plugins under the plugins directory. This structure allows easy addition or removal of commands without modifying the core application logic.

**Logging and History Management:** The application logs each executed command to a CSV file in the csv/ directory. This approach supports tracking command usage, which could be valuable for debugging or usage analysis.

**Design Patterns and Their Impact**

**Command Pattern:**

Implementation: Each command (AddCommand, DivideCommand) implements the Command abstract base class. The execute method serves as the main entry point for performing each command’s unique functionality.

Impact: This pattern provides a uniform interface for all commands, making it easy to manage and invoke commands dynamically. It also supports future scalability, as new commands can be added without altering existing code.

**Factory Pattern (for Plugin Loading):**

Implementation: The CommandHandler class dynamically loads command plugins using the importlib module. The plugins are registered based on their module and class names.
