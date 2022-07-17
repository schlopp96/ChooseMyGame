#!/usr/bin/env python3

import sys
from os import chdir
from os.path import dirname

sys.path.insert(0, dirname(
    dirname(__file__)))  # Ensure module can be found by Python.

chdir(dirname(__file__))  # Change working directory to main module.

from ChooseMyGame.appGUI.gui import window, sg

__version__ = '0.1.0'


def activate_GUI():
    while True:
        event, values = window.read()

        if event in [sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Exit']:
            break

    window.close()  # Close the window and return resources to the OS


def main():
    activate_GUI()


if __name__ == "__main__":
    main()