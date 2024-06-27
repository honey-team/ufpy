import os

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
    ...

def repo(repo: str, download_path: str, branch_name: str = 'main'):
    ...

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
