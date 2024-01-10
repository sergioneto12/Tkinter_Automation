# Multi-App Launcher

This Python application enables users to create a list of executable programs on a Windows operating system and open multiple programs simultaneously by activating the code.

## Requirements

- Python 3.x
- Tkinter (Python's standard GUI library)

## Installation

No specific installation is required beyond having Python installed.

## Usage

1. Run the Python script.
2. Click on the "Open file" button to select executable files. The selected files will be displayed on the window.
3. To execute all the selected programs, click on the "Run" button.
4. To clear the list of selected programs, click on the "Clear" button.

## How it works

- The application uses Tkinter for the graphical user interface.
- Upon execution, the window allows users to add executable files by using the "Open file" button.
- The selected files are displayed on the window.
- Clicking the "Run" button executes all the selected programs simultaneously.
- The "Clear" button removes all the selected programs from the list.

## Notes

- The list of selected programs is saved in the `save.txt` file.
- The `save.txt` file contains a comma-separated list of file paths.
- On subsequent runs, previously selected programs will be loaded from `save.txt`.

## Contributing

Feel free to contribute to the development of this application by submitting pull requests or reporting issues.

## License

This project is licensed under the [MIT License](LICENSE).

