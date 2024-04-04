# OSRS PyAutoGUI Willow Tree AI

![OSRS Bot](https://static.wikia.nocookie.net/2007scape/images/a/a3/Macros.gif/revision/latest?cb=20141201090409)

## Description

This is a Python script that uses PyAutoGUI to automate the process of cutting down trees and banking the logs in Old School RuneScape (OSRS). The bot utilizes AI image detection to identify trees and the banking interface to perform these actions.

## Features

- Automatically detects and interacts with trees.
- Deposits logs into the bank.
- Customizable settings for different tree types and banking locations. ⚠️(COMING SOON)⚠️
- User-friendly and easy to configure.

## Status
[![run_tests](https://github.com/maddox05/osrsAI-pyautogui/actions/workflows/python-app.yml/badge.svg)](https://github.com/maddox05/osrsAI-pyautogui/actions/workflows/python-app.yml)

## Prerequisites

Before using this bot, make sure you have the following prerequisites installed:

- Python 3.x: You can download it from [python.org](https://www.python.org/downloads/).
- PyAutoGUI: Install it using `pip install pyautogui`.
- Pillow (PIL): Install it using `pip install pillow`.
- PyClick: Install it using `pip install pyclick`.
- OpenCV: Install it using `pip install opencv-python`.
- Currently only works on Windows. MacOS and Linux support coming soon.

## Installation

1. Clone this repository to your local machine or download it as a ZIP file and extract it.
2. Open a terminal/command prompt and navigate to the project directory.

## Usage

1. Run the bot by executing the `main.py` script using Python:
```
python main.py
```

2. Make sure you have Old School RuneScape running in the foreground and your character is at the desired location.

3. The bot will start detecting trees, cutting them down, and banking the logs according to your configuration.

4. To stop the bot, exit the application.

## Disclaimer

**USE AT YOUR OWN RISK**: This bot interacts with the OSRS client using AI image detection, which may violate the game's terms of service. Using this bot may result in your account being banned. Be sure to review and comply with Jagex's terms of service before using this bot.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the OSRS community.
- Thanks to the developers of PyAutoGUI and Pillow for their fantastic libraries.
- Special thanks to the OSRS Wiki for providing information about tree locations and banking spots.

