import io
import os
from shutil import copy, copytree, rmtree
from tempfile import gettempdir
from typing import Iterable
from zipfile import ZipFile

from requests import get

from ufpy.path import UOpen

__all__ = (
    'file',
    'folder',
    'repo',
    'UGithubDownloader',
)

def file(repository: str, file_path: str | list[str], download_path: str, branch_name: str = 'main'):
    with UGithubDownloader(repository, download_path, branch_name) as gd:
        if isinstance(file_path, str):
            gd.download_file(file_path)
        else:
            gd.download_files(file_path)

def folder(repository: str, folder_path: str | list[str], download_path: str, branch_name: str = 'main'):
    with UGithubDownloader(repository, download_path, branch_name) as gd:
        if isinstance(folder_path, str):
            gd.download_folder(folder_path)
        else:
            gd.download_folders(folder_path)

def repo(repository: str, download_path: str, branch_name: str = 'main'):
    with UGithubDownloader(repository, download_path, branch_name) as gd:
        gd.download_repo()


def format_paths(*paths: str | list[str]) -> str | list[str] | list[list[str]]:
    new_paths = []
    for path in paths:
        if isinstance(path, list):
            path = format_paths(*path)
        else:
            path = path.replace('\\', '/')

            if path.startswith('/'):
                path = path[1:]
            if path.endswith('/'):
                path = path[:-1]

        new_paths.append(path)
    return new_paths[0] if len(new_paths) <= 1 else new_paths


CWD = os.getcwd()

class UGithubDownloader:
    """
    Class for downloading GitHub repositories, folders and files from it.
    """
    def __init__(self, repository: str, base_download_path: str = CWD, branch_name: str = 'main'):
        """
        Init UGithubDownloader

        Arguments:
        - repo: Repository author and name (ex. 'honey-team/ufpy')
        - base_download_path: Path where you want to download files from repository (ex. '~/repo'). Default is current
        working directory. Note: all methods will download file into this path (download_repo('/ufpy') will download
        repo into '~/repo/ufpy'
        - branch_name: Name of branch to download
        """
        self.__repo = repository
        self.__base_download_path = format_paths(base_download_path)
        self.__branch = branch_name
        self.__zip = None
        self.__repo_path = None

    def __enter__(self):
        url = f'https://github.com/{self.__repo}/archive/{self.__branch}.zip'
        r = get(url, timeout=10)

        if not r.ok:
            r.raise_for_status()

        self.__zip = ZipFile(io.BytesIO(r.content))

        temp_dir = format_paths(gettempdir())
        self.__zip.extractall(temp_dir)
        repo_name = self.__repo.split('/')[-1]
        self.__repo_path = f'{temp_dir}/{repo_name}-{self.__branch}'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__zip.close()
        if os.path.exists(self.__repo_path):
            rmtree(self.__repo_path)

    def download_file(self, file_path: str, download_path: str = ''):
        """
        Download file from GitHub repository.

        Arguments:
        - file_path: Path in repository to download (example, 'message.txt')
        - download_path: Path where will be downloaded file.
        """
        file_path, download_path = format_paths(file_path, download_path)
        download_path = f'{self.__base_download_path}/{download_path}'

        url = f'https://raw.githubusercontent.com/{self.__repo}/{self.__branch}/{file_path}'
        r = get(url, timeout=10)

        if not r.ok:
            r.raise_for_status()

        path = f'{download_path}/{file_path}'

        with UOpen(path, 'w+') as f:
            f.write(r.text)

    def download_files(self, file_paths: Iterable[str], download_path: str = ''):
        """
        Download files from GitHub repository.

        Arguments:
        - file_paths: Paths in repository to download (example, ['message.txt', 'README.md']).
        - download_path: Path where will be downloaded files.
        """
        file_paths, download_path = format_paths(list(file_paths), download_path)
        for file_path in file_paths:
            self.download_file(file_path, download_path)

    def download_folder(self, folder_path: str, download_path: str = ''):
        """
        Download folder from GitHub repository.

        Arguments:
        - folder_path: Path in repository to download (example, 'docs').
        - download_path: Path where will be downloaded files.
        """
        download_path = format_paths(download_path)
        download_path = f'{self.__base_download_path}/{download_path}'

        src, dst = f'{self.__repo_path}/{folder_path}', f'{download_path}/{folder_path}'
        if os.path.exists(dst):
            rmtree(dst)
        copytree(src, dst)

    def download_folders(self, folder_paths: Iterable[str], download_path: str = ''):
        """
        Download folders from GitHub repository.

        Arguments:
        - folder_paths: Paths in repository to download (example, ['docs', '.github']).
        - download_path: Path where will be downloaded files.
        """
        folder_paths, download_path = format_paths(list(folder_paths), download_path)
        for folder_path in folder_paths:
            self.download_folder(folder_path, download_path)

    def download_repo(self, download_path: str = ''):
        """
        Download all repository.

        Arguments:
        - download_path: Path where will be downloaded repository.
        """
        download_path = format_paths(download_path)
        download_path = f'{self.__base_download_path}/{download_path}'

        for filename in os.listdir(self.__repo_path):
            src, dst = f'{self.__repo_path}/{filename}', f'{download_path}/{filename}'
            if os.path.isdir(src):
                if os.path.exists(dst):
                    rmtree(dst)
                copytree(src, dst)
            else:
                if os.path.exists(dst):
                    os.remove(dst)
                copy(src, dst)
