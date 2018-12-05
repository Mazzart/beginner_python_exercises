"""Script shows the list of files and directories"""

from os import listdir, getcwd


def current_files_directories(path: str=getcwd()):
    """Print the list of files and directories.
    Print the list of files and directories for the entered path
    otherwise print result for the current working directory.
    """

    result = [item for item in listdir(path)]

    print(f'List of files and directories in {path}: {result}')
