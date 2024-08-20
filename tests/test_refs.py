import unittest
from unittest.mock import patch, mock_open
from collections import OrderedDict
from gitlib.objects.refs import create_ref, get_refs, resolve_refs, show_refs
from gitlib.repo import repo_create
import os

class TestGitModule(unittest.TestCase):

    def test_create_ref(self, mock_repo_file, mock_file):
        print(os.path.curdir)
        self.repo = repo_create("test_repo")
        mock_repo_file.return_value = "/fake/path/refs/heads/master"
        create_ref(self.repo, "1234567", "heads/master")
        
        mock_repo_file.assert_called_once_with(self.repo, "refs/", "heads/master")
        mock_file.assert_called_once_with("/fake/path/refs/heads/master", "w")
        mock_file().write.assert_called_once_with("1234567/")

    def test_get_refs(self, mock_repo_file, mock_resolve_refs, mock_isdir, mock_listdir):
        mock_repo_file.return_value = "/fake/path/refs"
        mock_listdir.return_value = ["heads", "tags"]
        mock_isdir.side_effect = lambda path: path.endswith("heads") or path.endswith("tags")
        mock_resolve_refs.return_value = "fake_sha"

        refs = get_refs(self.repo)

        mock_repo_file.assert_called_once_with(self.repo, "refs")
        self.assertIsInstance(refs, OrderedDict)
        self.assertIn("heads", refs)
        self.assertIn("tags", refs)

    def test_resolve_refs(self, mock_repo_file, mock_isfile, mock_file):
        mock_repo_file.return_value = "/fake/path/refs/heads/master"
        mock_isfile.return_value = True
        
        result = resolve_refs(self.repo, "refs/heads/master")

        mock_repo_file.assert_called_once_with(self.repo, "refs/heads/master")
        mock_isfile.assert_called_once_with("/fake/path/refs/heads/master")
        mock_file.assert_called_once_with("/fake/path/refs/heads/master", "r")
        self.assertEqual(result, "fake_sha")

    @patch("gitlib.objects.refs.show_refs")
    def test_show_refs(self, mock_show_refs):
        refs = OrderedDict({
            "heads": "fake_sha1",
            "tags": "fake_sha2"
        })

        show_refs(refs)
        
        mock_show_refs.assert_called_once_with(refs, "")

if __name__ == "__main__":
    unittest.main()
