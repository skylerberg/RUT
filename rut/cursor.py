from rut.observer import Observable


class Cursor(Observable):

    def __init__(self, pane):
        super(Cursor, self).__init__()
        self.pane = pane
        self._row = 0
        self._col = 0

    @property
    def row(self):
        return self._row

    @row.setter
    @Observable.notify_after
    def row(self, value):
        self._row = value

    @property
    def col(self):
        return self._col

    @col.setter
    @Observable.notify_after
    def col(self, value):
        self._col = value
        self.notify_observers()

    def get_cursor(self):
        return self.row, self.col

    def move_down(self):
        self.row = min(self.pane.get_line_count() - 1, self.row + 1)
        column_count = len(self.pane.get_lines()[self.row])
        self.col = max(min(column_count - 1, self.col), 0)

    def move_up(self):
        self.row = max(0, self.row - 1)
        column_count = len(self.pane.get_lines()[self.row])
        self.col = max(min(column_count - 1, self.col), 0)

    def move_right(self):
        column_count = len(self.pane.get_lines()[self.row])
        self.col = max(min(column_count - 1, self.col + 1), 0)

    def move_left(self):
        self.col = max(0, self.col - 1)

    def move_insert_right(self):
        column_count = len(self.pane.get_lines()[self.row])
        self.col = max(min(column_count, self.col + 1), 0)

    def goto_first_row(self):
        self.row = 0

    def goto_last_row(self):
        self.row = len(self.pane.get_lines()) - 1

    def goto_first_column(self):
        self.col = 0

    def goto_last_column(self):
        self.col = len(self.pane.get_lines()[self.row]) - 1
