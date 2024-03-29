# Guess The Number Telegram Bot

Welcome to the Guess The Number Telegram Bot, an interactive game where players attempt to guess a randomly selected number within a specified range. This bot is designed to provide users with a fun and engaging way to pass time, challenge their intuition, and improve their guessing skills.

## Features

- **Interactive Gameplay**: Users interact with the bot through simple text commands to start playing, make guesses, or choose to play later.
- **Dynamic Difficulty**: Each game session features a randomly generated number within a dynamic range, ensuring every game is unique.
- **Real-Time Feedback**: Players receive immediate feedback on their guesses to help guide them towards the correct number.
- **Performance Tracking**: The game calculates points based on the number of attempts and the time taken to guess the number, adding a competitive edge to the game.
- **Session Persistence**: Game progress, such as the number of attempts and the elapsed time, is tracked seamlessly during the session.

## Version History

- **Version 1.2**: Introduced a scoring system based on the formula `points = ((100/"number of attempts") + (100/"game time"))`. Added notifications for earned points.
- **Version 1.1**: Conducted minor code refactoring. Added tracking for the time spent on the game.
- **Version 1.0**: Initial release. The bot can challenge players to guess a number and confirm if the guess is correct. Results are recorded in a file.

## Getting Started

To use this bot, you'll need to have a Telegram account. Start a conversation with the bot by searching for its Telegram username or clicking on a direct link (if provided).

### Commands

- `/start`: Initiates the bot and presents the user with the option to play the game or defer it to later.
- Text commands: The bot responds to "Играть" to start the game, "Позже" to defer the game, and numeric inputs for guesses.

## Installation

This bot is built using the Python Telegram Bot API. To run your own instance of this bot:

1. Clone this repository or download the source code.
2. Ensure you have Python installed on your system.
3. Install the required packages by running `pip install pyTelegramBotAPI`.
4. Replace `TOKEN` in the script with your bot's unique API token obtained from BotFather.
5. Run the script using `python script_name.py`.

## Contributing

Feedback and contributions are highly appreciated! If you have any suggestions for improvements or have identified bugs, feel free to fork the repository, make your changes, and submit a pull request.
