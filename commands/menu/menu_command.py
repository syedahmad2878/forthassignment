from calc_app.commands.command import Command

class menuCommand(Command):
    def execute(self):
        print("greet")
        print("goodbye")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        print("exit")