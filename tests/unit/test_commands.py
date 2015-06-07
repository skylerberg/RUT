# pylint: disable=too-many-public-methods
import unittest

import rut.commands

class TestCommands(unittest.TestCase):

    def test_quit(self):
        with self.assertRaises(SystemExit):
            rut.commands.quit()
