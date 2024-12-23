import os
import tarfile
from commands import CommandHandler

class ShellEmulator:
    def __init__(self, username, hostname, tar_file_path):
        self.username = username
        self.hostname = hostname
        self.current_path = "/"
        self.virtual_fs = self._load_virtual_fs(tar_file_path)
        self.command_handler = CommandHandler(self)

    def _load_virtual_fs(self, tar_file_path):
    fs = {}
    with tarfile.open(tar_file_path, 'r') as tar:
        for member in tar.getmembers():
            # даляем './' из имени файла
            clean_name = member.name.lstrip('./')
            if member.isfile():
                file_obj = tar.extractfile(member)
                try:
                    content = file_obj.read().decode('utf-8') if file_obj else None
                except UnicodeDecodeError:
                    content = None  
                fs[clean_name] = content
            else:
                fs[clean_name] = None  
    return fs
    
    def execute_command(self, command):
        return self.command_handler.execute(command)

    def prompt(self):
        return f"{self.username}@{self.hostname}:{self.current_path}$ "
