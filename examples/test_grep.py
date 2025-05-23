import os
import unittest

from files import grep


CONTENT = """hello world
bye hello
how are you?
bye bye
oh hi hello there
"""


class GretTestCase(unittest.TestCase):
    FILENAME = "test_file.txt"

    @classmethod
    def setUpClass(cls):
        with open(cls.FILENAME, "w") as f:
            f.write(CONTENT)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.FILENAME)

    def test_text_found_in_multiple_lines(self):
        result = grep("hello", self.FILENAME)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, [
            "hello world\n",
            "bye hello\n",
            "oh hi hello there\n",
        ])

    def test_text_not_found(self):
        result = grep("not found", self.FILENAME)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            grep("not found", "nonexistent.txt")
