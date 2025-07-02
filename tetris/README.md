# Tetris Game

This project implements the classic Tetris game in a command-line interface.

## How to Play

1.  Execute the script from your terminal:
    ```bash
    python tetris_game.py
    ```
2.  The game will automatically drop pieces. The goal is to clear lines by filling them completely with blocks.

## Features

-   **CLI-based Graphics:** Renders the game board and pieces using text characters.
-   **Piece Generation:** Generates random Tetris pieces (tetrominoes).
-   **Piece Movement:** Pieces automatically fall. (Note: User input for movement and rotation is not yet implemented in this CLI version).
-   **Line Clearing:** Detects and clears full lines, shifting blocks down.
-   **Score Tracking:** Keeps track of the player's score.
-   **Game Over Condition:** Ends the game when pieces stack up to the top.

## Notes

This is a basic implementation focusing on the core game mechanics. For a fully interactive game, input handling for moving and rotating pieces would need to be added.