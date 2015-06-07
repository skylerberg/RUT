class Pane(object):

    def __init__(self, contents="", path=None):
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
        self.row = 0
        self.col = 0
        self.line_count = None
        self.subscribers = []

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

    def append(self, string):
        self.lines += string.split('\n')
        self.__notify_subscribers()

    def move(self, direction):
        if direction == "down":
            self.row = min(self.get_line_count() - 1, self.row + 1)
            self.col = max(min(len(self.lines[self.row]) -1, self.col), 0)
        elif direction == "up":
            self.row = max(0, self.row - 1)
            self.col = max(min(len(self.lines[self.row]) -1, self.col), 0)
        elif direction == "right":
            self.col = max(min(len(self.lines[self.row]) - 1, self.col + 1), 0)
        elif direction == "left":
            self.col = max(0, self.col - 1)
        self.__notify_subscribers()

    def get_line_count(self):
        return len(self.lines)

    def get_cursor(self):
        return self.row, self.col

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def replace(self, row, col, char):
        line = self.lines[row]
        self.lines[row] = line[:col] + char + line[col + 1:]
        self.__notify_subscribers()

    def get_lines(self):
        return self.lines

    def __notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.notify(self)

    def __str__(self):
        return '\n'.join(self.lines)
