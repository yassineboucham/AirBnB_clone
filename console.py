#!/usr/bin/python3

"""create the console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """the Command of HBNB"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors."""
        return True

    def do_help(self, arg: str) -> bool | None:
        """To get help on a command, type help <topic>."""
        return super().do_help(arg)

    def emptyline(self):
        """Override default `empty line + return` behaviour."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
