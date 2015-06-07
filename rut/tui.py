import curses

class Tui(object):

    def __init__(self, pane):
        self.screen = self._build_screen()
        curses.curs_set(1)
        curses.noecho()
        pane.add_subscriber(self)
        self.screen.scrollok(1)
        self.display_pane(pane)

    def _build_screen(self):
        return curses.initscr()

    def notify(self, pane):
        self.display_pane(pane)

    def display_pane(self, pane):
        self.screen.clear()
        self._draw_string(str(pane))
        self.screen.move(*pane.get_cursor())
        self.screen.refresh()

    def set_cursor(self, row, col):
        self.screen.set_cursor(row, col)

    def _draw_string(self, string):
        rows, _ = self.screen.getmaxyx()
        lines = self.__split_into_lines(string)
        for i, line in enumerate(lines):
            if i == rows - 1:
                break
            self.screen.addstr(i, 0, line)

    def __split_into_lines(self, string):
        _, cols = self.screen.getmaxyx()
        full_lines = string.split("\n")
        lines = []
        for line in full_lines:
            if len(line) < cols:
                lines.append(line)
            else:
                for i in range(0, len(line), cols):
                    lines.append(line[i:i + cols])
        return lines

    def get_input(self):
        return self.screen.getch()

    def end(self):
        curses.endwin()
