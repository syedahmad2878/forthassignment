from calc_app.commands.command import Command

class subCommand(Command):
    def execute(self):
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        try:
            c = float(a) - float(b)
            print(f"The result is: {c}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")