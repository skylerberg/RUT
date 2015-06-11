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
