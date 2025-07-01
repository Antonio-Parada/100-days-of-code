import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.laps = []
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.running = False
            print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")
            return elapsed_time
        else:
            print("Stopwatch is not running.")
            return None

    def reset(self):
        self.start_time = None
        self.laps = []
        self.running = False
        print("Stopwatch reset.")

    def lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            self.laps.append(lap_time)
            print(f"Lap {len(self.laps)}: {lap_time:.2f} seconds.")
        else:
            print("Stopwatch is not running. Start it to record laps.")

    def display_time(self):
        if self.running:
            current_time = time.time() - self.start_time
            print(f"Current time: {current_time:.2f} seconds.")
        elif self.start_time is not None:
            print(f"Last recorded time: {self.laps[-1]:.2f} seconds." if self.laps else "Stopwatch is stopped.")
        else:
            print("Stopwatch is not started.")

if __name__ == "__main__":
    stopwatch = Stopwatch()
    print("--- CLI Stopwatch App ---")
    print("Commands: start, stop, reset, lap, show, exit")

    while True:
        command = input("> ").lower()

        if command == "start":
            stopwatch.start()
        elif command == "stop":
            stopwatch.stop()
        elif command == "reset":
            stopwatch.reset()
        elif command == "lap":
            stopwatch.lap()
        elif command == "show":
            stopwatch.display_time()
        elif command == "exit":
            print("Exiting stopwatch.")
            break
        else:
            print("Unknown command.")
