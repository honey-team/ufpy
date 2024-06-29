# GitHub / Download

## Introduction

In `ufpy` there are 3 functions and 1 class for downloading things from public GitHub repositories.
You can download an entire repository, a folder or multiple folders, and a file or multiple files without
a GitHub token. You can use the `UGithubDownloader` class for all these actions or the other 3 functions.
The class is more optimized for multiple requests. If you need to download multiple times, use it. It uses
an unpacked zip archive for all operations and deletes it at the end. If you don't want to download anything
multiple times, use the functions instead.

Import functions and class from `ufpy`:
```python
import ufpy
from ufpy import UGithubDownloader, download_file, download_folder, download_repo, UGithubDownloader
```

> [!CAUTION]
> All repositories you want to download from must be public

## Open `UGithubDownloader` class and use it

To open this class, you should use the `with` operator as you do with files and other resources:
```python
with UGithubDownloader("honey-team/ufpy", "C:/Ufpy-Test", "0.1") as gd:
    # First argument - "repository owner"/"repository name"
    # Second - Base download path (all methods use download paths relative to the base download path, similar to how it works in the command line.
    # For example: base path: C:\; cd ufpy -> final path: C:\ufpy.) (default is the current working directory)
    # Third argument: Branch or tag name (default is "main" (not master!))
    gd.download_repo() # In C:/Ufpy-Test will appear all files from 0.1 tag in this repository.
    gd.download_repo("ufpy-0.1") # In C:/Ufpy-Test/ufpy-0.1 will appear all files from 0.1 tag in this repository
```

## Download file(s)

You can use `download_file()` function, `ufpy.github.download.file()` function
(they're the same, but with different names) and `UGithubDownloader.download_file()` method.

> [!NOTE]
> You can use any iterable of strings in `download_file()` function for downloading several files.
> In `UGithubDownloader`, there is a `download_files()` method.

One file:
```python
download_file("honey-team/ufpy", "README.md", "C:/Users/<name>/ufpy-tests")
# copy README.md from the main branch to the C:/Users/<name>/ufpy-tests directory

with UGithubDownloader("honey-team/ufpy", "C:/Users/<name>/ufpy-tests") as gd:
    gd.download_file("README.md") # Same
```

After changing `<name>` to your username and running this code you'll get this:
![Download one file](.assets/download1.png)

Two files:
```python
download_file("honey-team/ufpy", ["README.md", "mkdocs.yml"], "C:/Users/<name>/ufpy-tests")
# copy README.md and mkdocs.yml from main branch in C:/Users/<name>/ufpy-tests directory

with UGithubDownloader("honey-team/ufpy", "C:/Users/<name>/ufpy-tests") as gd:
    gd.download_files(["README.md", "mkdocs.yml"]) # Same
```

After changing `<name>` to your username and running this code you'll get this:
![Download two files](.assets/download2.png)

## Download folder(s)

You can use `download_folder()` function, `ufpy.github.download.folder()` function
(they're same, but with different names) and `UGithubDownloader.download_folder()` method.

> [!NOTE]
> You can use any iterable of strings in `download_folder()` function for downloading several folders.
> In `UGithubDownloader` there are `download_folders()` method.

One folder:
```python
download_folder("honey-team/ufpy", "examples", "C:/Users/<name>/ufpy-tests")
# create the C:/Users/<name>/ufpy-tests/examples folder
# and copy origin/examples contents from main branch in this folder

with UGithubDownloader("honey-team/ufpy", "C:/Users/<name>/ufpy-tests") as gd:
    gd.download_folder("examples") # Same
```

After changing `<name>` to your username and running this code you'll get this:
![Download one folder](.assets/download3.png)

Two folders:
```python
download_folder("honey-team/ufpy", ["examples", ".github"], "C:/Users/<name>/ufpy-tests")
# create C:/Users/<name>/ufpy-tests/examples and C:/Users/<name>/ufpy-tests/.github folders
# and copy origin/examples contents and origin/.github contents from main branch in this folders

with UGithubDownloader("honey-team/ufpy", "C:/Users/<name>/ufpy-tests") as gd:
    gd.download_folders(["examples", ".github"]) # Same
```

After changing `<name>` to your username and running this code you'll get this:
![Download two folders](.assets/download4.png)

## Download all repository

You can use `download_repo()` function, `ufpy.github.download.repo()` function
(they're same, but with different names) and `UGithubDownloader.download_repo()` method:
```python
download_repo("honey-team/ufpy", "C:/Users/<name>/ufpy-tests")
# copy all repository files and folders with its contents from main branch in C:/Users/<name>/ufpy-tests directory.

with UGithubDownloader("honey-team/ufpy", "C:/Users/<name>/ufpy-tests") as gd:
    gd.download_repo() # Same
```

After changing `<name>` to your username and running this code you'll get this:

> [!NOTE]
> The repository code shown is from before merging this pull request
> ([#37](https://github.com/honey-team/ufpy/pull/37)).
> When this pull request was merged, repository was changed.

![Download all repository](.assets/download5.png)
