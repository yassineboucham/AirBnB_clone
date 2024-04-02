#!/usr/bin/python3

"""create the console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """the Command of HBNB"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Ctrl + D stops the console"""
        return True

    def do_quit(self, line):
        """quit command will exit the console"""
        return True

    def emptyline(self):
        """Do nothing when getting an empty line"""
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
