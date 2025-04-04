"""
Library for simplifying working with GitHub.

Key features:
- Download repositories, files, folders from GitHub public repositories.
"""

# Download
import ufpy.github.download
from ufpy.github.download import UGithubDownloader
from ufpy.github.download import file as download_file
from ufpy.github.download import folder as download_folder
from ufpy.github.download import repo as download_repo
