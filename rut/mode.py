import abc

import rut.keys as keys
from rut.trie import HashTrie

class Mode(object):
    """
    Mode objects represent the mode that a Controller is using to interpret
    commands. This is basically the state pattern.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, controller):
        self.controller = controller
        self.pane = self.controller.get_pane()
        self.current_command = ""
        self.commands = HashTrie()

    def send_key(self, key):
        self.current_command += key
        if self.current_command in self.commands:
            self.commands[self.current_command]()
            self.current_command = ""
        while self.current_command and \
                not self.commands.prefix_match(self.current_command):
            self.current_command = self.current_command[1:]

    def switch_to(self, mode):
        self.controller.mode = mode(self.controller)


def _steps(*functions):
    def __call_all():
        for function in functions:
            function()
    return __call_all

class ExMode(Mode):

    def __init__(self, controller):
        super(ExMode, self).__init__(controller)
        self.commands = HashTrie({
                "q": exit,
                "w": self.pane.save,
                "wq": _steps(
                    self.pane.save,
                    exit),
                })


    def send_key(self, key):
        if key == '\n':
            if self.current_command in self.commands:
                self.commands[self.current_command]()
            self.switch_to(NormalMode)
        self.current_command += key


class NormalMode(Mode):

    def __init__(self, controller):
        super(NormalMode, self).__init__(controller)
        self.commands = HashTrie({
                ":": lambda: self.switch_to(ExMode),
                "i": lambda: self.switch_to(InsertMode),
                "a": _steps(
                    lambda: self.switch_to(InsertMode),
                    self.pane.move_insert_right,
                    ),
                "A": _steps(
                    self.pane.goto_last_column,
                    lambda: self.switch_to(InsertMode),
                    self.pane.move_insert_right,
                    ),
                "gI": _steps(
                    self.pane.goto_first_column,
                    lambda: self.switch_to(InsertMode),
                    ),
                "r": lambda: self.switch_to(ReplaceMode),
                "h": self.pane.move_left,
                "j": self.pane.move_down,
                "k": self.pane.move_up,
                "l": self.pane.move_right,
                "G": self.pane.goto_last_row,
                "gg": self.pane.goto_first_row,
                "0": self.pane.goto_first_column,
                "$": self.pane.goto_last_column,
                })

class ReplaceMode(Mode):

    def send_key(self, key):
        row, col = self.pane.get_cursor()
        self.pane.replace(row, col, key)
        self.switch_to(NormalMode)


class InsertMode(Mode):

    def __init__(self, controller):
        super(InsertMode, self).__init__(controller)
        self.commands = HashTrie({
                keys.ESC: lambda: self.switch_to(NormalMode),
                })

    def send_key(self, key):
        if key in self.commands:
            self.commands[key]()
        else:
            row, col = self.pane.get_cursor()
            self.pane.insert(row, col, key)
            self.pane.move_insert_right()
