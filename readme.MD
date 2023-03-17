# GuessThePin Bot

This is a bot that automatically guesses pins on [GuessThePin](https://www.guessthepin.com/) website. The bot uses Selenium and Firefox webdriver to automate the guessing process. The bot is divided into multiple threads that run concurrently, and each thread is responsible for guessing a specific range of pins. This approach is taken to speed up the process and maximize the number of guesses per second.

## Prerequisites

- Python 3.x
- Selenium
- Firefox Webdriver
- Discord API token (optional)

## Installation

1. Clone the repository from GitHub
2. Install Selenium and Discord API module using pip

```bash
pip install selenium==3.0.0
pip install discord
```
3. Download the latest Firefox webdriver from [here]([https://www.guessthepin.com/](https://github.com/mozilla/geckodriver/releases)), or use the in this repo.
4. Extract the geckodriver executable to a directory and note down the path.

## Usage
1. Open the guessthepin_bot.py file in a text editor
2. Modify the executable_path variable to the path of the geckodriver executable on your system.
3. (Optional) Replace the Discord API token with your own to receive notifications when the program completes.
4. Save the file and run it using the following command:
```bash
python guessthepin_bot.py
```
## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your changes.
