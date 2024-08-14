# Rock-Paper-Scissors Game

## Description

This repository contains two implementations of the classic Rock-Paper-Scissors game in Python. Both implementations allow a player to compete against the computer, with the game determining the winner based on the rules of Rock-Paper-Scissors.

### Implementation 1: Simple Rock-Paper-Scissors

This implementation provides a basic version of the game where the player chooses Rock, Paper, or Scissors, and the computer makes a random choice. The result is then displayed, and the player has the option to play again or exit.

### Implementation 2: Rock-Paper-Scissors with Scoring

This implementation extends the basic game to include scoring over multiple rounds. The player and computer each get points based on their choices, and the game determines a winner after a set number of rounds.

## Features

- **Command-line Interface**: Both implementations run in the terminal.
- **Random Computer Choice**: Computer makes random choices each round.
- **Replay Option**: Allows players to play multiple rounds or games.

## Requirements

- **Python 3.x** must be installed on your system.

## How to Run

1. **Download or clone the repository.**
2. **Navigate to the directory containing the desired script (`rock_paper_scissors_simple.py` or `rock_paper_scissors_scoring.py`).**

### Running Implementation 1: Simple Rock-Paper-Scissors

```bash
python rock_paper_scissors_simple.py
```

**Game Instructions:**
- Enter your choice (Rock: 0, Paper: 1, Scissors: 2).
- The computer will make its choice, and the result will be displayed.
- You can choose to continue playing or exit after each round.

### Running Implementation 2: Rock-Paper-Scissors with Scoring

```bash
python rock_paper_scissors_scoring.py
```

**Game Instructions:**
- Enter your choice (Rock, Paper, or Scissors).
- The computer will make its choice, and the round result will be displayed.
- The game will keep track of scores over three rounds and declare a winner at the end.

## Code Overview

### Implementation 1: Simple Rock-Paper-Scissors

- **`generate_computer_choice()`**: Generates a random choice for the computer (0-2).
- **`check_win_lose(player_choice, computer_choice)`**: Determines the result of the round.
- **`play()`**: Manages user input and game logic for a single round.
- **`rock_paper_scissor_game()`**: Handles the game flow, including replay options.

### Implementation 2: Rock-Paper-Scissors with Scoring

- **`get_comp_choice()`**: Generates a random choice for the computer (rock, paper, or scissors).
- **`get_user_choice()`**: Prompts the user for input and validates it.
- **`play_round()`**: Plays a single round and returns the points.
- **`main()`**: Runs the game, keeping track of scores over three rounds and determining the winner.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as you like.

## Contributing

If you have suggestions for improvements or would like to contribute to this project, please feel free to fork the repository and submit a pull request.

## Contact

For any questions or feedback, please reach out to [ritabratopani29@gmail.com].
