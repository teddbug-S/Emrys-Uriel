import os
# import shutil
import re
from functools import cached_property
from pathlib import Path
from win32com import client
from pprint import pprint


class JunkDetector:
    """
        Finds Junk file on the specified Drive.

        First try to detect uninstalled program leftovers.
                                                         """

    def __init__(self, drive=os.environ['SYSTEMDRIVE']) -> None:
        self.DRIVE = drive

    @cached_property
    def _initialized_paths(self):
        """ 
        Initialize the needed directories for the search

        :return: a tuple of pathlib.Path() --> WindowsPath objects
        :rtype: Tuple
        """
        _start_menu = Path(os.environ['PROGRAMDATA'] + r"\Microsoft\Windows\Start Menu\Programs")
        _start_menu_user = Path(os.environ['APPDATA'] + r"\Microsoft\Windows\Start Menu\Programs")

        return _start_menu, _start_menu_user

    def find_programs(self):

        _path_names = self._initialized_paths
        _shallow_paths = self._exclude_win([_paths for _path_name in _path_names for _paths in _path_name.iterdir() if
                                            _paths.is_dir()])
        _programs = {}
        for _path in _shallow_paths:
            for _file in _path.glob('**/*.lnk'):
                _programs[os.path.basename(_path)] = self._confirm_exists(_file)

        pprint(_programs)

    @staticmethod
    def _exclude_win(paths) -> list:
        """ 
        Excludes some important Windows directories from our search

        :param paths: [description] paths found.
        :type paths: [type] List.
        :return: [description] paths (filtered)
        :rtype: [type] List

        """
        _excludes = [
            'Windows PowerShell',
            'System Tools',
            'Administrative Tools',
            'Accessories',
            'Accessibility',
            'StartUp',
            'Maintenance',
            'Control Panel'
            'OneDrive'  # not really needed
            # some programs have links to docs, websites and stuff, not needed.
            r'(https://\w+\.(com|org|io|docs)$|http://\w+$\.(com|org|io|docs)$|www.\w+\.(com|org|io|docs)$)'
        ]

        for _exclude in _excludes:
            _pattern = re.compile(f'{_exclude}', re.IGNORECASE)
            for path in paths:
                if _pattern.search(str(path)):
                    paths.remove(path)
        return paths

    @staticmethod
    def _confirm_exists(file):
        shell = client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(str(file))
        return os.path.exists(shortcut.Targetpath)


myjunk = JunkDetector()
myjunk.find_programs()
