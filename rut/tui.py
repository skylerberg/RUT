import curses

class Tui(object):

    def __init__(self, pane):
        self.screen = self._build_screen()
        self.pane = pane
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
            physical += length / self.__width()
        physical += logical_col / self.__width()
        return physical, logical_col % self.__width()

    def _build_screen(self):
        return curses.initscr()

    def notify(self, pane):
        self.display_pane(pane)

    def display_pane(self, pane):
        self.screen.clear()
        self._draw_string(str(pane))
        self.set_cursor(*pane.get_cursor())
        self.screen.refresh()

    def set_cursor(self, logical_row, logical_col):
        row, col = self._get_physical_position(logical_row, logical_col)
        self.screen.move(row, col)

    def _draw_string(self, string):
        rows, _ = self.screen.getmaxyx()
        lines = self.__split_into_lines(string)
        for i, line in enumerate(lines):
            if i == rows - 1:
                break
            self.screen.addstr(i, 0, line)

    def __width(self):
        height, width = self.screen.getmaxyx()
        return width

    def __height(self):
        height, width = self.screen.getmaxyx()
        return width

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
        return self.screen.getch()

    def end(self):
        curses.endwin()
