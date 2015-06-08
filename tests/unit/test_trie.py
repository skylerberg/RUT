# pylint: disable=too-many-public-methods
import unittest

from rut.trie import HashTrie

class TestHashTrie(unittest.TestCase):

    def setUp(self):
        self.trie = HashTrie()

    def test_find_empty_string(self):
        self.assertFalse("" in self.trie)

    def test_add_empty_string(self):
        self.trie[""] = ""
        self.assertTrue("" in self.trie)


class TestPopulatedHashTrie(unittest.TestCase):

    def setUp(self):
        self.in_trie = set(["norma", "normal"])
        self.trie = HashTrie(normal=True, norma=False)

    def test_items_in_trie(self):
        for item in self.in_trie:
            self.assertTrue(item in self.trie)

    def test_is_prefix(self):
        self.assertTrue(self.trie.prefix_match("norm"))

    def test_is_not_prefix(self):
        self.assertFalse(self.trie.prefix_match("nqrm"))

    def test_whole_word_is_prefix(self):
        self.assertTrue(self.trie.prefix_match("normal"))
