# pylint: disable=too-many-public-methods
import unittest

from rut.pane import Pane
from rut.cursor import Cursor


class TestCursor(unittest.TestCase):

    def setUp(self):
        self.pane = Pane(contents="line one\nline two\nline three")
        self.cursor = Cursor(self.pane)

    def test_get_cursor(self):
        self.assertEquals((0, 0), self.cursor.get_cursor())

    def test_move_down(self):
        self.cursor.move_down()
        self.assertEquals((1, 0), self.cursor.get_cursor())

    def test_move_right(self):
        self.cursor.move_right()
        self.assertEquals((0, 1), self.cursor.get_cursor())

    def test_move_left(self):
        self.cursor.move_left()
        self.assertEquals((0, 0), self.cursor.get_cursor())

    def test_move_up(self):
        self.cursor.move_up()
        self.assertEquals((0, 0), self.cursor.get_cursor())

    def test_move_right_and_left(self):
        self.cursor.move_right()
        self.cursor.move_left()
        self.assertEquals((0, 0), self.cursor.get_cursor())

    def test_move_down_and_up(self):
        self.cursor.move_down()
        self.cursor.move_up()
        self.assertEquals((0, 0), self.cursor.get_cursor())

    def test_move_below_last_line(self):
        self.cursor.move_down()
        self.cursor.move_down()
        self.cursor.move_down()
        self.assertEquals((2, 0), self.cursor.get_cursor())

    def test_move_past_last_col(self):
        pane = Pane(contents="12\n34\n56")
        cursor = Cursor(pane)
        cursor.move_right()
        cursor.move_right()
        self.assertEquals((0, 1), cursor.get_cursor())

    def test_goto_last_row(self):
        self.cursor.goto_last_row()
        self.assertEquals((2, 0), self.cursor.get_cursor())

    def test_goto_first_row(self):
        self.cursor.goto_first_row()
        self.assertEquals((0, 0), self.cursor.get_cursor())

    def test_goto_first_column(self):
        self.cursor.move_right()
        self.cursor.move_right()
        self.cursor.goto_first_column()
        self.assertEquals((0, 0), self.cursor.get_cursor())

    def test_goto_last_column(self):
        self.cursor.goto_last_column()
        self.assertEquals((0, 7), self.cursor.get_cursor())
