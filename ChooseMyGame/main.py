#!/usr/bin/env python3

import sys
from os import chdir
from os.path import dirname
from typing import NoReturn

sys.path.insert(0, dirname(
    dirname(__file__)))  # Ensure module can be found by Python.

chdir(dirname(__file__))  # Change working directory to main module.

from ChooseMyGame.appGUI.gui import sg, window
from ChooseMyGame.appLogger.logger import logger

__version__ = '0.1.0'

textborder: str = f'\n<{"*" * 121}>\n'  # Text border.


def activate_GUI() -> None:
    while True:
        event, values = window.read()  # Read GUI event.

        logger.info(f'{event} {values}')

        print(event, values)  # Enable for easier debugging

        if event in [sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Exit']:
            break

    window.close()  # Close the window and return resources to the OS.


def main() -> None:
    logger.info(f'Started ChooseMyGame v{__version__}...')

    activate_GUI()  # Start program window.

    return program_exit(0)  # Exit program.


def program_exit(code: int) -> NoReturn | None:
    logger.info(f'Exiting program...\n{textborder}')

    return sys.exit(code)  # Exit program.


if __name__ == "__main__":
    main()
