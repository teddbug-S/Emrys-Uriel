import os
import shutil
import re
from functools import cached_property
from pathlib import Path
from win32com import client
from pprint import pprint

class JunkDetector:
    """
        Finds Junk file on the specified Drive.

        First try to detect unistalled program leftovers.
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
        _start_menu = Path(os.environ['PROGRAMDATA']+r"\Microsoft\Windows\Start Menu\Programs")
        _start_menu_user = Path(os.environ['APPDATA']+r"\Microsoft\Windows\Start Menu\Programs")

        return _start_menu, _start_menu_user
    
    
    def find_programs(self):

        _path_names = self._initialized_paths
        # initialize with programs without dirs for shortcut
        _lnk_files = self._exclude_win([file for _path_name in _path_names for file in _path_name.glob('*.lnk')])
        # discover paths to .lnk file of supposed to be programs but not proven thus the name _shallow_paths
        _shallow_paths = self._exclude_win([_dir_name for _path_name in _path_names\
            for _dir_name in _path_name.iterdir() if not _dir_name.is_file()])
        
        _lnk_files.extend([ file for _path_name in _shallow_paths for file in _path_name.glob('**/*.lnk')])
        _existing_programs = {program.stem: self._confirm_exists(str(program)) for program in _lnk_files if self._confirm_exists(str(program))}

        # pprint(_existing_programs)

    
    def _exclude_win(self, paths)  -> None:
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
        'OneDrive' # not really needed
        # some programs have links to docs, websites and stuff, not needed.
        r'(https://\w+\.(com|org|io|docs)$|http://\w+$\.(com|org|io|docs)$|www.\w+\.(com|org|io|docs)$)'
        ]

        for _exclude in _excludes:
            _pattern = re.compile(f'{_exclude}', re.IGNORECASE)
            for path in paths:
                if _pattern.search(str(path)):
                    paths.remove(path)
        return paths


    def _confirm_exists(self, file):
        shell = client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(file)
        return Path(shortcut.targetpath).exists() and os.path.splitext(shortcut.targetpath) == '.exe'

