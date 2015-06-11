import curses

import rut.keys as keys


class Tui(object):

    def __init__(self, pane):
        self.screen = curses.initscr()
        self.pane = pane
        self.scroll = 0
        curses.curs_set(1)
        curses.noecho()
        pane.add_subscriber(self)
        self.screen.scrollok(1)
        self.display_pane(pane)

    def _get_physical_position(self, logical_row, logical_col):
        physical = logical_row
        for line_number, line in enumerate(self.pane.get_lines()):
            if line_number == logical_row:
                break
            length = len(line) - 1  # Don't count newline
            if length > self.__width():
                physical += length / self.__width()
        physical += logical_col / self.__width()
        return physical, logical_col % self.__width()

    def notify(self, pane):
        self.display_pane(pane)

    def display_pane(self, pane):
        self.screen.clear()
        self.set_scroll(*pane.get_cursor())
        self._draw_string(str(pane))
        self.set_cursor(*pane.get_cursor())
        self.screen.refresh()

    def set_scroll(self, logical_row, logical_col):
        row, _ = self._get_physical_position(logical_row, logical_col)
        height = self.__height()
        if row < self.scroll:
            self.scroll = row
        if row >= self.scroll + height - 1:
            self.scroll += row - (height + self.scroll) + 2

    def set_cursor(self, logical_row, logical_col):
        row, col = self._get_physical_position(logical_row, logical_col)
        self.screen.move(row - self.scroll, col)

    def _draw_string(self, string):
        height = self.__height()
        lines = self.__split_into_lines(string)
        for i, line in enumerate(lines):
            if i == self.scroll + height - 1:
                break
            if i >= self.scroll:
                self.screen.addstr(i - self.scroll, 0, line)

    def __width(self):
        _, width = self.screen.getmaxyx()
        return width

    def __height(self):
        height, _ = self.screen.getmaxyx()
        return height

    def __split_into_lines(self, string):
        width = self.__width()
        full_lines = string.split("\n")
        lines = []
        for line in full_lines:
            if len(line) < width:
                lines.append(line)
            else:
                for i in range(0, len(line), width):
                    lines.append(line[i:i + width])
        return lines

    def get_input(self):
        result = self.screen.getch()
        if result == 27:
            self.screen.nodelay(True)
            next_char = self.screen.getch()  # TODO handle it if it is alt
            self.screen.nodelay(False)
            if next_char == -1:
                return keys.ESC
        return chr(result)

    def end(self):  # pylint: disable=no-self-use
        curses.endwin()
