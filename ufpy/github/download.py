import io
import os
from shutil import copy, copytree, rmtree
from tempfile import gettempdir
from typing import Iterable
from zipfile import ZipFile

import requests

from ufpy.path import UOpen

__all__ = (
    'file',
    'folder',
    'repo',
    'UGithubDownloader',
)

def file(repo: str, file_path: str | list[str], download_path: str, branch_name: str = 'main'):
    with UGithubDownloader(repo, download_path, branch_name) as gd:
        if isinstance(file_path, str):
            gd.download_file(file_path)
        else:
            gd.download_files(file_path)

def folder(repo: str, folder_path: str | list[str], download_path: str, branch_name: str = 'main'):
    with UGithubDownloader(repo, download_path, branch_name) as gd:
        if isinstance(folder_path, str):
            gd.download_folder(folder_path)
        else:
            gd.download_folders(folder_path)

def repo(repo: str, download_path: str, branch_name: str = 'main'):
    with UGithubDownloader(repo, download_path, branch_name) as gd:
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
    def __init__(self, repo: str, base_download_path: str = CWD, branch_name: str = 'main'):
        self.__repo = repo
        self.__base_download_path = format_paths(base_download_path)
        self.__branch = branch_name

    def __enter__(self):
        url = f'https://github.com/{self.__repo}/archive/{self.__branch}.zip'
        r = requests.get(url, timeout=10)

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
        file_path, download_path = format_paths(file_path, download_path)
        download_path = f'{self.__base_download_path}/{download_path}'

        url = f'https://raw.githubusercontent.com/{self.__repo}/{self.__branch}/{file_path}'
        r = requests.get(url)

        if not r.ok:
            r.raise_for_status()

        path = f'{download_path}/{file_path}'

        with UOpen(path, 'w+') as f:
            f.write(r.text)

    def download_files(self, file_paths: Iterable[str], download_path: str = ''):
        file_paths, download_path = format_paths(list(file_paths), download_path)
        for file_path in file_paths:
            self.download_file(file_path, download_path)

    def download_folder(self, folder_path: str, download_path: str = ''):
        download_path = format_paths(download_path)
        download_path = f'{self.__base_download_path}/{download_path}'

        src, dst = f'{self.__repo_path}/{folder_path}', f'{download_path}/{folder_path}'
        if os.path.exists(dst):
            rmtree(dst)
        copytree(src, dst)

    def download_folders(self, folder_paths: Iterable[str], download_path: str = ''):
        folder_paths, download_path = format_paths(list(folder_paths), download_path)
        for folder_path in folder_paths:
            self.download_folder(folder_path, download_path)

    def download_repo(self, download_path: str = ''):
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
