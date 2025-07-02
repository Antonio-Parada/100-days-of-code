# Memory Puzzle Game

This project implements the classic Memory Puzzle game in a command-line interface.

## How to Play

1.  Execute the script from your terminal:
    ```bash
    python memory_puzzle.py
    ```
2.  The game will display a board of hidden cards. Enter the row and column for two cards to reveal them. If they match, they remain revealed; otherwise, they flip back.
3.  The goal is to match all pairs in the fewest attempts possible.

## Features

-   **CLI-based Graphics:** Renders the game board using text characters.
-   **Random Board Generation:** Shuffles and places card pairs randomly on the board.
-   **Match Detection:** Identifies matching card pairs.
-   **Attempt Tracking:** Counts the number of attempts made.
-   **Game Over Condition:** Ends the game when all pairs are matched.

## Notes

This is a basic implementation. For a more visually rich experience, a graphical user interface would be beneficial.