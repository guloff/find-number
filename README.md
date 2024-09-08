# Telegram Number Guessing Game Bot

## Description

This Python script is a Telegram bot that allows users to play a number guessing game. The bot randomly generates a number within a specified range, and the user tries to guess it. The bot tracks the number of attempts and the time taken for each game, then calculates a score based on the formula:  
`score = (100 / number of attempts) + (100 / game time in seconds)`.  
Results are stored in a JSON file, including the number of attempts, game time, and points.

## Features

- **Random Number Guessing**: The bot generates a random number, and users try to guess it.
- **Real-time Feedback**: The bot provides feedback after each attempt, telling users if the guess was too high or too low.
- **Score Calculation**: The final score is calculated based on the number of attempts and the time spent.
- **Leaderboard**: Game results are saved to a `leaderboard.json` file, recording user ID, number of attempts, game time, and score.
- **Simple Commands**: Users can start the game with a simple "Играть" command and can delay playing with "Позже".

## Requirements

- **Python 3.x**
- **pyTelegramBotAPI**: A Python wrapper for the Telegram Bot API.

### Install Dependencies

Install the required libraries using pip:

```bash
pip install pyTelegramBotAPI
```

## Usage

1. **Create a Telegram Bot**:
   - Go to [BotFather](https://t.me/BotFather) in Telegram and create a new bot.
   - Get the API token for your bot.

2. **Configure the Token**:
   - In the script, replace the `TOKEN` variable with your actual Telegram bot API token.

3. **Run the Bot**:
   - Run the script using Python:

   ```bash
   python bot.py
   ```

4. **Interact with the Bot**:
   - Send `/start` to the bot to initiate the interaction.
   - Choose "Играть" to start the number guessing game.
   - The bot will generate a random number, and you can start guessing by sending numbers.
   - The bot will give feedback on whether your guess is too high or too low.
   - Once you guess correctly, the bot will display the number of attempts, the time taken, and the score.

### Example

1. **Start the Game**:
   ```text
   Привет, <Name>! Поиграем? Сможете угадать число, которое я загадал? Нажмите 'Играть', чтобы начать игру.
   ```
2. **Receive Feedback**:
   ```text
   Попытка №1. Нет, маловато. Загаданное число больше 450.
   ```
3. **Game Results**:
   ```text
   Поздравляю! Вы угадали число за 5 попыток, потратив на игру 30 секунд. Количество заработанных баллов - 18.5.
   ```

## JSON Leaderboard Format

Game results are saved in `leaderboard.json` with the following structure:

```json
{
    "user_id": 123456789,
    "user_first_name": "John",
    "user_last_name": "Doe",
    "tries": 5,
    "gametime": 30,
    "starttime": 1660000000.0,
    "points": 18.5
}
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for more details.
