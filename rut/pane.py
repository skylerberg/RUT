from rut.text import TextRegion
from rut.observer import Observable, Observer


class Pane(Observable, Observer):

    def __init__(self, contents="", path=None):
        super(Pane, self).__init__()
        self.text = TextRegion()
        self.path = path
        if path is not None:
            self.lines = []
            with open(path, 'a+') as file_:
                file_contents = file_.read()
                if file_contents and file_contents[-1]:
                    file_contents = file_contents[:-1]
                self.text.append(file_contents)
        elif contents:
            self.text.append(contents)

    def notify(self, observable):
        self.notify_observers()

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
        self.text.append(string)

    def get_line_count(self):
        return len(self.text.get_lines())

    def replace(self, row, col, char):
        self.text.replace(row, col, char)

    def insert(self, row, col, char):
        self.text.insert(row, col, char)

    def get_lines(self):
        return self.text.get_lines()

    def __str__(self):
        return str(self.text)
