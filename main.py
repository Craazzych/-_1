import sys
from shell_emulator import ShellEmulator
from gui import ShellGUI

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <username> <hostname> <tar_file_path>")
        sys.exit(1)

    username = sys.argv[1]
    hostname = sys.argv[2]
    tar_file_path = sys.argv[3]

    shell = ShellEmulator(username, hostname, tar_file_path)
    gui = ShellGUI(shell)
    gui.run()

if __name__ == "__main__":
    main()
