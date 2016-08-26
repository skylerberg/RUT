class Movement(object):

    def __init__(self, pane):
        self.pane = pane
        self.start = Position()
        self.end = Position()

    def __str__(self):
        self.string = self.pane.text.substring(self.start, self.end)

    def operate(self, function):
        self.update(function(str(self)))

    def update(self, string):
        self.pane.text.delete(self.start, self.end)
        self.pane.text.insert(self.start, string)


class Position(object):

    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
