import unittest
from os import remove
from tempfile import gettempdir

import ufpy
from ufpy import UGithubDownloader, download_file


class UGithubDownloadTestCase(unittest.TestCase):
    def test_file(self):
        repo = 'honey-team/ufpy'
        file = 'README.md'

        temp_dir = gettempdir()
        download_path = rf'{temp_dir}\ufpy-tests'
        file_path = rf'{download_path}\README.md'

        # download_file()
        download_file(repo, file, download_path)

        with open(file_path, 'r') as f:
            file_contents1 = f.read()

        remove(file_path)

        # file()
        ufpy.github.download.file(repo, file, download_path)

        with open(file_path, 'r') as f:
            file_contents2 = f.read()

        remove(file_path)

        # UGithubDownloader.download_file()
        with UGithubDownloader(repo, download_path) as gd:
            gd.download_file(file)

        with open(file_path, 'r') as f:
            file_contents3 = f.read()

        remove(file_path)

        # Asserts
        self.assertEqual(file_contents1, file_contents2)
        self.assertEqual(file_contents1, file_contents3)
        self.assertEqual(file_contents2, file_contents3)


if __name__ == '__main__':
    unittest.main()
