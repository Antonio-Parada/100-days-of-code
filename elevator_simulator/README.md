# Elevator Simulator

This project implements a basic command-line elevator simulation.

## How to Use

1.  Execute the script from your terminal:
    ```bash
    python elevator_simulator.py
    ```
2.  Enter floor numbers (0-4) to request the elevator. Type 'q' to quit.

## Features

-   **Floor Requests:** Users can request the elevator to specific floors.
-   **Movement Logic:** The elevator moves between floors, picking up and dropping off passengers based on requests.
-   **Directional Movement:** The elevator prioritizes requests in its current direction of travel.
-   **CLI Visualization:** Displays the elevator's current floor, direction, and pending requests.

## Notes

This is a simplified simulation. Advanced features like multiple elevators, capacity limits, and more complex scheduling algorithms are not implemented.