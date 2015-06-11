# pylint: disable=too-many-public-methods
import unittest

from rut.pane import Pane


class TestPane(unittest.TestCase):

    def test_create(self):
        self.assertTrue(Pane())

    def test_create_from_file(self):
        path = "tests/fixtures/fox.txt"
        pane = Pane(path=path)
        with open(path) as file_:
            self.assertEqual(pane.save_preview(), file_.read())

    def test_medium_size_file(self):
        path = "tests/fixtures/100_lines.txt"
        pane = Pane(path=path)
        with open(path) as file_:
            self.assertEqual(pane.save_preview(), file_.read())

    def test_create_from_string(self):
        test_content = "This is a test"
        pane = Pane(contents=test_content)
        self.assertEqual(test_content, str(pane))

    def test_append(self):
        test_content = "This is a test"
        pane = Pane()
        pane.append(test_content)
        self.assertEqual(test_content, str(pane))

    def test_save_no_path_specified(self):
        test_content = "This is a test"
        pane = Pane(contents=test_content)
        self.assertRaises(TypeError, pane.save)

    def test_get_cursor(self):
        pane = Pane()
        self.assertEquals((0, 0), pane.get_cursor())

    def test_replace_at_end_of_pane(self):
        pane = Pane(contents="a\ntest")
        pane.replace(1, 3, 's')
        self.assertEquals("a\ntess", str(pane))

    def test_lines(self):
        pane = Pane(contents="line one\nline two")
        self.assertEquals(pane.get_lines()[0], "line one")

    def test_replace(self):
        pane = Pane(contents="line one\nline two")
        pane.replace(0, 0, 'w')
        self.assertEquals("wine one\nline two", str(pane))

    def test_get_line_count(self):
        pane = Pane(contents="line one\nline two")
        self.assertEquals(2, pane.get_line_count())


class TestNavigation(unittest.TestCase):

    def setUp(self):
        self.pane = Pane(contents="line one\nline two\nline three")

    def test_move_down(self):
        self.pane.move_down()
        self.assertEquals((1, 0), self.pane.get_cursor())

    def test_move_right(self):
        self.pane.move_right()
        self.assertEquals((0, 1), self.pane.get_cursor())

    def test_move_left(self):
        self.pane.move_left()
        self.assertEquals((0, 0), self.pane.get_cursor())

    def test_move_up(self):
        self.pane.move_up()
        self.assertEquals((0, 0), self.pane.get_cursor())

    def test_move_right_and_left(self):
        self.pane.move_right()
        self.pane.move_left()
        self.assertEquals((0, 0), self.pane.get_cursor())

    def test_move_down_and_up(self):
        self.pane.move_down()
        self.pane.move_up()
        self.assertEquals((0, 0), self.pane.get_cursor())

    def test_move_below_last_line(self):
        self.pane.move_down()
        self.pane.move_down()
        self.pane.move_down()
        self.assertEquals((2, 0), self.pane.get_cursor())

    def test_move_past_last_col(self):
        pane = Pane(contents="12\n34\n56")
        pane.move_right()
        pane.move_right()
        self.assertEquals((0, 1), pane.get_cursor())

    def test_goto_last_row(self):
        self.pane.goto_last_row()
        self.assertEquals((2, 0), self.pane.get_cursor())

    def test_goto_first_row(self):
        self.pane.goto_first_row()
        self.assertEquals((0, 0), self.pane.get_cursor())

    def test_goto_first_column(self):
        self.pane.move_right()
        self.pane.move_right()
        self.pane.goto_first_column()
        self.assertEquals((0, 0), self.pane.get_cursor())

    def test_goto_last_column(self):
        self.pane.goto_last_column()
        self.assertEquals((0, 7), self.pane.get_cursor())


class TestObserverPattern(unittest.TestCase):

    def notify(self, publisher):
        """
        To test the observer pattern on the pane, I am using the self-shunt
        pattern inside this test case.
        """
        self.notified_by = publisher

    def setUp(self):
        self.notified_by = None
        self.pane = Pane(contents="some\ntext")
        self.pane.add_subscriber(self)

    def test_append_notifies(self):
        self.pane.append("")
        self.assertEquals(self.pane, self.notified_by)

    def test_replace_notifies(self):
        self.pane.replace(0, 0, "a")
        self.assertEquals(self.pane, self.notified_by)
