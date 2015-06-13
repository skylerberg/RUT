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
            self.assertEqual(file_.read(), pane.save_preview())

    def test_medium_size_file(self):
        path = "tests/fixtures/100_lines.txt"
        pane = Pane(path=path)
        with open(path) as file_:
            self.assertEqual(file_.read(), pane.save_preview())

    def test_create_from_string(self):
        test_content = "This is a test"
        pane = Pane(contents=test_content)
        self.assertEqual(test_content, str(pane))

    def test_save_no_path_specified(self):
        test_content = "This is a test"
        pane = Pane(contents=test_content)
        self.assertRaises(TypeError, pane.save)
