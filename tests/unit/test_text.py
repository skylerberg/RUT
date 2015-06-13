# pylint: disable=too-many-public-methods
import unittest

from rut.text import TextRegion


class TestText(unittest.TestCase):

    def setUp(self):
        self.text = TextRegion()

    def test_append(self):
        test_content = "This is a test"
        self.text.append(test_content)
        self.assertEqual(test_content, str(self.text))

    def test_replace_at_end_of_pane(self):
        self.text.append("a\ntest")
        self.text.replace(1, 3, 's')
        self.assertEquals("a\ntess", str(self.text))

    def test_lines(self):
        self.text.append("line one\nline two")
        self.assertEquals(self.text.get_lines()[0], "line one")

    def test_replace(self):
        self.text.append("line one\nline two")
        self.text.replace(0, 0, 'w')
        self.assertEquals("wine one\nline two", str(self.text))

    def test_get_line_count(self):
        self.text.append("line one\nline two")
        self.assertEquals(2, self.text.get_line_count())
