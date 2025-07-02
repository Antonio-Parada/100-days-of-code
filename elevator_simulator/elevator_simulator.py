import time
import os

class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 0  # Start at ground floor
        self.direction = None  # 'UP', 'DOWN', or None (idle)
        self.requests = []  # List of requested floors

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_status(self):
        self._clear_screen()
        print("Elevator Status")
        print(f"Current Floor: {self.current_floor}")
        print(f"Direction: {self.direction if self.direction else 'Idle'}")
        print(f"Requests: {sorted(self.requests)}")
        print("\n" + "-" * 20)
        for floor in range(self.num_floors - 1, -1, -1):
            if floor == self.current_floor:
                print(f"| {'E' if self.direction else ' '} | Floor {floor}")
            else:
                print(f"|   | Floor {floor}")
        print("-" * 20)

    def request_floor(self, floor):
        if 0 <= floor < self.num_floors:
            if floor not in self.requests:
                self.requests.append(floor)
                self.requests.sort()
                print(f"Request received for Floor {floor}")
            else:
                print(f"Floor {floor} already requested.")
        else:
            print("Invalid floor request.")

    def _move(self):
        if not self.requests:
            self.direction = None
            return

        if self.direction == 'UP':
            if self.current_floor < self.requests[-1]: # Move towards highest request
                self.current_floor += 1
            else:
                self.direction = 'DOWN' # Change direction if highest request passed
                self.current_floor -= 1
        elif self.direction == 'DOWN':
            if self.current_floor > self.requests[0]: # Move towards lowest request
                self.current_floor -= 1
            else:
                self.direction = 'UP' # Change direction if lowest request passed
                self.current_floor += 1
        else: # Idle, set initial direction
            if self.requests[0] > self.current_floor:
                self.direction = 'UP'
                self.current_floor += 1
            elif self.requests[0] < self.current_floor:
                self.direction = 'DOWN'
                self.current_floor -= 1
            else: # Already at requested floor
                self.requests.remove(self.current_floor)
                print(f"Stopped at Floor {self.current_floor}")

    def simulate(self, steps=20, initial_requests=None):
        if initial_requests:
            for req_floor in initial_requests:
                self.request_floor(req_floor)

        for _ in range(steps):
            self.display_status()
            self._move()
            if self.current_floor in self.requests:
                self.requests.remove(self.current_floor)
                print(f"Stopped at Floor {self.current_floor}")
            time.sleep(0.5)

        print("Simulation finished.")

if __name__ == '__main__':
    elevator = Elevator(num_floors=5)
    print("--- Interactive Elevator Simulation ---")
    print("Enter floor numbers to request the elevator. Type 'q' to quit.")

    while True:
        try:
            user_input = input("Enter floor request (0-4, or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Exiting simulation.")
                break
            
            floor = int(user_input)
            elevator.request_floor(floor)
            elevator.simulate(steps=1) # Simulate one step per request

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4, or 'q'.")
        except KeyboardInterrupt:
            print("Exiting simulation.")
            break