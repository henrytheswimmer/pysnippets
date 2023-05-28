import unittest
from main import add_snippet, view_snippets, search_snippets, edit_snippet, delete_snippet
from snippet import Snippet, CODE_SNIPPETS, SnippetNotFoundError
from unittest.mock import patch
from io import StringIO

# python3 -m unittest test_snippet.py

class SnippetTestCase(unittest.TestCase):
    def setUp(self):
        CODE_SNIPPETS.clear()

    def test_add_snippet(self):
        with patch("builtins.input", side_effect=["Title", "print('Hello, World!')", "Description", "tag1 tag2"]):
            add_snippet()

        self.assertEqual(len(CODE_SNIPPETS), 1)
        self.assertEqual(CODE_SNIPPETS[0].title, "Title")
        self.assertEqual(CODE_SNIPPETS[0].snippet, "print('Hello, World!')")
        self.assertEqual(CODE_SNIPPETS[0].desc, "Description")
        self.assertListEqual(CODE_SNIPPETS[0].tags, ["tag1", "tag2"])
    
    def test_view_snippets(self):
        CODE_SNIPPETS.append(Snippet("Title 1", "x = 1", "Description 1", ["tag1"]))
        CODE_SNIPPETS.append(Snippet("Title 2", "x = 2", "Description 2", ["tag2", "tag3"]))
        expected_output = [
            "Title: Title 1",
            "Snippet: x = 1",
            "Description: Description 1",
            "Tags: ['tag1']",
            "Title: Title 2",
            "Snippet: x = 2",
            "Description: Description 2",
            "Tags: ['tag2', 'tag3']"
        ]

        with patch("sys.stdout", new=StringIO()) as fake_output:
            view_snippets()
            actual_output = fake_output.getvalue().strip()
            
            for snippet_detail in expected_output:
                self.assertIn(snippet_detail, actual_output)

    def test_search_snippets(self):
        pass

    def test_edit_snippet(self):
        pass

    def test_delete_snippet(self):
        pass

