from rut.observer import Observable


class Pane(Observable):

    def __init__(self, contents="", path=None):
        super(Pane, self).__init__()
        self.path = path
        if path is not None:
            self.lines = []
            with open(path, 'a+') as file_:
                for line in file_:
                    self.lines.append(line.rstrip('\n'))
        elif contents:
            self.lines = contents.split('\n')
        else:
            self.lines = []
        self.line_count = None

    def save_preview(self):
        """
        Get the string representing the buffer to be written to a file.

        If the buffer is not empty, then a newline will be added to the end of
        the file as is consistent with editors like vim. This makes the file
        work better with programs like cat.
        """
        content = str(self)
        if content:
            content += '\n'
        return content

    def save_as(self, path):
        with open(path, 'w') as file_:
            file_.write(self.save_preview())

    def save(self):
        self.save_as(self.path)

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
