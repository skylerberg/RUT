from rut.observer import Observable


class Cursor(Observable):

    def __init__(self, pane):
        super(Cursor, self).__init__()
        self.pane = pane
        self.row = 0
        self.col = 0

    def get_cursor(self):
        return self.row, self.col

    def move_down(self):
        self.row = min(self.pane.get_line_count() - 1, self.row + 1)
        self.col = max(min(len(self.pane.lines[self.row]) - 1, self.col), 0)
        self.notify_subscribers()

    def move_up(self):
        self.row = max(0, self.row - 1)
        self.col = max(min(len(self.pane.lines[self.row]) - 1, self.col), 0)
        self.notify_subscribers()

    def move_right(self):
        self.col = max(min(len(self.pane.lines[self.row]) - 1, self.col + 1),
                       0)
        self.notify_subscribers()

    def move_left(self):
        self.col = max(0, self.col - 1)
        self.notify_subscribers()

    def move_insert_right(self):
        self.col = max(min(len(self.pane.lines[self.row]), self.col + 1), 0)
        self.notify_subscribers()

    def goto_first_row(self):
        self.row = 0
        self.notify_subscribers()

    def goto_last_row(self):
        self.row = len(self.pane.lines) - 1
        self.notify_subscribers()

    def goto_first_column(self):
        self.col = 0
        self.notify_subscribers()

    def goto_last_column(self):
        self.col = len(self.pane.lines[self.row]) - 1
        self.notify_subscribers()
