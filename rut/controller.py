from rut.mode import NormalMode
from rut.pane import Pane
from rut.cursor import Cursor


class Controller(object):

    def __init__(self, pane=None):
        if pane is None:
            pane = Pane()
        self.pane = pane
        self.cursor = Cursor(pane)
        self.mode = NormalMode(self)

    def send_key(self, key):
        self.mode.send_key(key)

    def send_keys(self, keys):
        for key in keys:
            self.send_key(key)

    def get_pane(self):
        return self.pane

    def get_cursor(self):
        return self.cursor
