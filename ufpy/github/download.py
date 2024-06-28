import os
from shutil import copy, copytree, rmtree
from zipfile import ZipFile

from requests import get

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

    download_path = download_path.replace('\\', '/')
    path = f'{download_path}/{file_path}'

    directory = '/'.join(path.split('/')[:-1])

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, 'w+') as f:
        f.write(r.text)

def folder(repo: str, folder_path: str, download_path: str, branch_name: str = 'main'):
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
    dir = f'{download_path}/{main_directory_name}/{folder_path}'
    new_dir = f'{download_path}/{folder_path}'

    if os.path.exists(new_dir):
        print(
            f"Warning ({new_dir}): Currently we don't support editing recursive folders if it's exists"
            "when repo directory was downloaded. Sorry, you can just delete all folders with same name as in"
            "repo before you use this function instead."
        )
    else:
        copytree(dir, new_dir)

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
        else:
            if os.path.exists(new_file_path):
                with open(new_file_path, 'w') as nf:
                    with open(file_path, 'r') as f:
                        nf.write(f.read())
            else:
                copy(file_path, new_file_path)

    if os.path.exists(f'{download_path}/{main_directory_name}'):
        rmtree(f'{download_path}/{main_directory_name}')


class UGithubDownloader:
    def __init__(self, repo: str, branch_name: str = 'main'):
        self.__repo = repo
        self.__branch = branch_name

    def download_file(self, file_path: str, download_path: str):
        file(self.__repo, file_path, download_path, self.__branch)

    def download_folder(self, folder_path: str, download_path: str):
        folder(self.__repo, folder_path, download_path, self.__branch)

    def download_repo(self, download_path: str):
        repo(self.__repo, download_path, self.__branch)
