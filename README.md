# Python Cricket Cup

## Description

Welcome to the **Python Cricket Cup**! This is a command-line game that combines elements of cricket with the classic Stone-Paper-Scissors game. Compete against the computer in a simulated cricket match where you can choose to bat or bowl and try to score the most runs or take the most wickets.

## Features

- **Command-line Interface**: Play directly in your terminal.
- **Dynamic Gameplay**: Choose to bat or bowl, and play multiple overs.
- **Score Tracking**: Keeps track of scores and wickets for both player and computer.
- **Replay Option**: Play another match or exit after a game.

## Requirements

- **Python 3.x** must be installed on your system.

## Installation

1. Download or clone this repository.
2. Ensure you have Python installed on your system.
3. Navigate to the directory containing `cricket.py`.

## How to Play

1. Run the game by executing the following command in your terminal:

   ```bash
   python cricket.py
   ```

2. **Register Your Name**: Enter your name to start playing.
3. **Toss**: Choose between "heads" or "tails" to win the toss and decide whether to bat or bowl.
4. **Play**:
   - If you choose to bat, try to score as many runs as possible before losing all your wickets.
   - If you choose to bowl, try to restrict the computer’s runs and take all its wickets.
5. **Match Outcome**: The game will display the result of the match and whether you won or lost.

## Example Output

```bash
***WELCOME TO THE PYTHON CRICKET CUP***

Register your name to play
John
Hi John

Let's toss :
Choose [heads/tails] heads
Congratulations! You won the toss...
You want to bat or ball?  bat
...
```

## Functions

- `player_name()`: Registers and greets the player.
- `get_comp_choice()`: Generates a random choice for the computer.
- `get_user_choice()`: Prompts the user for a choice and validates input.
- `toss()`: Handles the coin toss and match choice (bat or ball).
- `overs()`: Gets the number of overs for the match.
- `main()`: Controls the flow of the game, including batting and bowling logic.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as you like.

## Contributing

If you have suggestions for improvements or would like to contribute to this project, please feel free to fork the repository and submit a pull request.

## Contact

For any questions or feedback, please reach out to [your-email@example.com].
