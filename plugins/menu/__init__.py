from commands import Command
import os
import pkgutil

class MenuCommand(Command):
    def execute(self, params):
        plugins_package = 'plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            print(f"Plugins directory '{plugins_path}' not found.")
            return
        print("Commands: ")

        for _ , plugin_name, _ in pkgutil.iter_modules([plugins_path]):
            print(plugin_name)