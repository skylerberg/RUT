from rut.observer import Observable


class TextRegion(Observable):

    def __init__(self):
        super(TextRegion, self).__init__()
        self.lines = []

    @Observable.notify_after
    def append(self, string):
        self.lines += string.split('\n')

    def get_line_count(self):
        return len(self.lines)

    @Observable.notify_after
    def replace(self, row, col, char):
        line = self.lines[row]
        self.lines[row] = line[:col] + char + line[col + 1:]

    @Observable.notify_after
    def insert(self, row, col, char):
        line = self.lines[row]
        self.lines[row] = line[:col] + char + line[col:]

    def get_lines(self):
        return self.lines

    def __str__(self):
        return '\n'.join(self.lines)
