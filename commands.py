class CommandHandler:
    def __init__(self, shell):
        self.shell = shell
        self.commands = {
            "ls": self.ls,
            "cd": self.cd,
            "exit": self.exit_shell,
            "tac": self.tac,
            "uptime": self.uptime,
            "wc": self.wc,
        }

    def execute(self, command):
        cmd, *args = command.split()
        if cmd in self.commands:
            return self.commands[cmd](*args)
        return f"Command not found: {cmd}"

    def ls(self, *args):
        return "\n".join(self.shell.virtual_fs.keys())

    def cd(self, path):
        if path in self.shell.virtual_fs:
            self.shell.current_path = path
            return f"Changed directory to {path}"
        return f"No such directory: {path}"

    def exit_shell(self, *args):
        return "exit"

    def tac(self, file_name):
        if file_name not in self.shell.virtual_fs:
            return f"No such file: {file_name}"
        content = self.shell.virtual_fs[file_name]
        return "\n".join(reversed(content.splitlines()))

    def uptime(self, *args):
        import time
        return f"System uptime: {time.time()} seconds"

    def wc(self, file_name):
        if file_name not in self.shell.virtual_fs:
            return f"No such file: {file_name}"
        content = self.shell.virtual_fs[file_name]
        lines = len(content.splitlines())
        words = len(content.split())
        chars = len(content)
        return f"{lines} {words} {chars} {file_name}"
