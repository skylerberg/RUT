import abc

import rut.keys as keys

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

    @abc.abstractmethod
    def send_key(self, key):
        pass

    def switch_to(self, mode):
        self.controller.mode = mode(self.controller)


class ExMode(Mode):

    def __init__(self, controller):
        super(ExMode, self).__init__(controller)
        self.commands = {
                "q": exit,
                "w": self.pane.save,
                }


    def send_key(self, key):
        if key == '\n':
            if self.current_command in self.commands:
                self.commands[self.current_command]()
            self.switch_to(NormalMode)
        self.current_command += key


class NormalMode(Mode):

    def __init__(self, controller):
        super(NormalMode, self).__init__(controller)
        self.commands = {
                ":": lambda: self.switch_to(ExMode),
                "i": lambda: self.switch_to(InsertMode),
                "r": lambda: self.switch_to(ReplaceMode),
                "h": lambda: self.pane.move("left"),
                "j": lambda: self.pane.move("down"),
                "k": lambda: self.pane.move("up"),
                "l": lambda: self.pane.move("right"),
                }

    def send_key(self, key):
        if key in self.commands:
            self.commands[key]()


class ReplaceMode(Mode):

    def send_key(self, key):
        row, col = self.pane.get_cursor()
        self.pane.replace(row, col, key)
        self.switch_to(NormalMode)


class InsertMode(Mode):

    def __init__(self, controller):
        super(InsertMode, self).__init__(controller)
        self.commands = {
                keys.ESC: lambda: self.switch_to(NormalMode),
                }

    def send_key(self, key):
        if key in self.commands:
            self.commands[key]()
        else:
            row, col = self.pane.get_cursor()
            self.pane.insert(row, col, key)
            self.pane.move("insert-right")
