import io
import os
import warnings
from shutil import copy, copytree, rmtree
from tempfile import gettempdir
from typing import Iterable, TypeAlias
from zipfile import ZipFile

from requests import get

from ufpy.path import UOpen

__all__ = (
    'file',
    'folder',
    'repo',
    'UGithubDownloader',
)

def file(repo: str, file_path: str, download_path: str, branch_name: str = 'main'):
    file_path = file_path.replace('\\', '/')

    url = f'https://raw.githubusercontent.com/{repo}/{branch_name}/{file_path}'
    r = get(url)

    if not r.ok:
        raise Exception("Error with getting file from GitHub. Check that repo is public and that file path is correct.")

    download_path = download_path.replace('\\', '/')
    path = f'{download_path}/{file_path}'

    directory = '/'.join(path.split('/')[:-1])

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, 'w+') as f:
        f.write(r.text)

def folder(repo: str, folder_path: str | list[str], download_path: str, branch_name: str = 'main'):
    if isinstance(folder_path, str):
        folder_path = [folder_path]
    filename = f'{download_path}/repo_temp.zip'
    url = f'https://github.com/{repo}/archive/{branch_name}.zip'

    with open(filename, 'wb') as f:
        f.write(get(url).content)

    repo_name = repo.split('/')[-1]
    main_directory_name = f'{repo_name}-{branch_name}'

    with ZipFile(filename) as archive:
        for file in archive.namelist():
            if file.startswith(main_directory_name):
                archive.extract(file, download_path)

    if os.path.exists(filename):
        os.remove(filename)

    for fpath in folder_path:
        folder_dir = f'{download_path}/{main_directory_name}/{fpath}'
        new_folder_dir = f'{download_path}/{fpath}'

        if os.path.exists(new_folder_dir):
            warnings.warn(
                f"Warning ({new_folder_dir}): Currently we don't support editing recursive folders if it's exists"
                "when repo directory was downloaded. Sorry, you can just delete all folders with same name as in"
                "repo before you use this function instead."
            )
        else:
            copytree(folder_dir, new_folder_dir)

    if os.path.exists(f'{download_path}/{main_directory_name}'):
        rmtree(f'{download_path}/{main_directory_name}')

def repo(repo: str, download_path: str, branch_name: str = 'main'):
    filename = f'{download_path}/repo_temp.zip'
    url = f'https://github.com/{repo}/archive/{branch_name}.zip'

    with open(filename, 'wb') as f:
        f.write(get(url).content)

    repo_name = repo.split('/')[-1]
    main_directory_name = f'{repo_name}-{branch_name}'

    with ZipFile(filename) as archive:
        for file in archive.namelist():
            if file.startswith(main_directory_name):
                archive.extract(file, download_path)

    if os.path.exists(filename):
        os.remove(filename)

    repo_dir = f'{download_path}/{main_directory_name}'
    for file in os.listdir(repo_dir):
        file_path = f'{repo_dir}/{file}'
        new_file_path = f'{download_path}/{file}'
        if os.path.isdir(file_path):
            if os.path.exists(new_file_path):
                print(
                    f"Warning ({new_file_path}): Currently we don't support editing recursive folders if it's exists"
                    "when repo directory was downloaded. Sorry, you can just delete all folders with same name as in"
                    "repo before you use this function instead."
                )
                continue
            copytree(file_path, new_file_path)
        elif os.path.exists(new_file_path):
            with open(new_file_path, 'w') as nf:
                with open(file_path, 'r') as f:
                    nf.write(f.read())
        else:
            copy(file_path, new_file_path)

    if os.path.exists(f'{download_path}/{main_directory_name}'):
        rmtree(f'{download_path}/{main_directory_name}')


def format_paths(*paths: str | list[str]) -> list[str] | list[list[str]] | list[str | list[str]] | str:
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


CWD: TypeAlias = None

class UGithubDownloader:
    def __init__(self, repo: str, base_download_path: str = CWD, branch_name: str = 'main'):
        if base_download_path == CWD:
            base_download_path = format_paths(os.getcwd())
        self.__repo = repo
        self.__base_download_path = format_paths(base_download_path)
        self.__branch = branch_name

    def __enter__(self):
        url = f'https://github.com/{self.__repo}/archive/{self.__branch}.zip'
        self.__zip = ZipFile(io.BytesIO(get(url).content))

        temp_dir = format_paths(gettempdir())
        self.__zip.extractall(temp_dir)
        repo_name = self.__repo.split('/')[-1]
        self.__repo_path = f'{temp_dir}/{repo_name}-{self.__branch}'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__zip.close()
        if os.path.exists(self.__repo_path):
            rmtree(self.__repo_path)

    def __del__(self):
        self.__zip.close()
        if os.path.exists(self.__repo_path):
            rmtree(self.__repo_path)

    def download_file(self, file_path: str, download_path: str = ''):
        file_path, download_path = format_paths(file_path, download_path)
        download_path = f'{self.__base_download_path}/{download_path}'

        url = f'https://raw.githubusercontent.com/{self.__repo}/{self.__branch}/{file_path}'
        r = get(url)

        if not r.ok:
            raise Exception(
                "Error with getting file from GitHub. Check that repo is public and that file path is correct.")

        path = f'{download_path}/{file_path}'

        with UOpen(path, 'w+') as f:
            f.write(r.text)

    def download_files(self, file_paths: Iterable[str], download_path: str = ''):
        file_paths, download_path = format_paths(list(file_paths), download_path)
        for file_path in file_paths:
            self.download_file(file_path, download_path)

    def download_folder(self, folder_path: str | list[str], download_path: str):
        ...

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
