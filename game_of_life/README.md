# Conway's Game of Life

This project implements Conway's Game of Life, a cellular automaton, in a command-line interface.

## How to Play

1.  Execute the script from your terminal:
    ```bash
    python game_of_life.py
    ```
2.  The simulation will start with a randomly seeded grid and evolve through generations. Press `Ctrl+C` to stop the simulation.

## Features

-   **Cellular Automaton:** Simulates the rules of Conway's Game of Life.
-   **Random Seeding:** Initializes the grid with a random distribution of live and dead cells.
-   **CLI Visualization:** Renders the grid's evolution using text characters in the console.
-   **Wrap-around Edges:** Cells at the edges of the grid interact with cells on the opposite side.

## Notes

This is a basic implementation. More complex initial patterns, user interaction, and performance optimizations could be added.