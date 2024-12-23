import unittest
from shell_emulator import ShellEmulator

class TestShellCommands(unittest.TestCase):
    def setUp(self):
        self.shell = ShellEmulator("test_user", "test_host", "test_fs.tar")

    def test_ls(self):
        output = self.shell.execute_command("ls")
        self.assertIn("file1.txt", output)

    def test_cd(self):
        output = self.shell.execute_command("cd /dir")
        self.assertEqual(output, "Changed directory to /dir")

    def test_tac(self):
        output = self.shell.execute_command("tac file1.txt")
        self.assertEqual(output, "c\nb\na")

    def test_uptime(self):
        output = self.shell.execute_command("uptime")
        self.assertTrue(output.startswith("System uptime"))

    def test_wc(self):
        output = self.shell.execute_command("wc file1.txt")
        self.assertIn("3 3 6", output)

    def test_exit(self):
        output = self.shell.execute_command("exit")
        self.assertEqual(output, "exit")

if __name__ == "__main__":
    unittest.main()
