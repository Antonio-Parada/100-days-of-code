import time

class PomodoroClock:
    def __init__(self, work_minutes=25, break_minutes=5):
        self.work_duration = work_minutes * 60
        self.break_duration = break_minutes * 60
        self.current_phase = "work"
        self.is_running = False
        self.time_left = self.work_duration

    def _countdown(self):
        while self.time_left > 0 and self.is_running:
            mins, secs = divmod(self.time_left, 60)
            timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
            print(f"\r{self.current_phase.capitalize()} Time: {timer}", end="")
            time.sleep(1)
            self.time_left -= 1
        print("\r" + " " * 30, end="") # Clear line

    def start(self):
        self.is_running = True
        print(f"\nStarting {self.current_phase} phase ({self.work_duration // 60} minutes).")
        self._countdown()
        if self.time_left <= 0:
            print(f"\n{self.current_phase.capitalize()} phase finished!")
            self._switch_phase()

    def pause(self):
        self.is_running = False
        print("\nTimer paused.")

    def reset(self):
        self.is_running = False
        self.current_phase = "work"
        self.time_left = self.work_duration
        print("\nTimer reset.")

    def _switch_phase(self):
        if self.current_phase == "work":
            self.current_phase = "break"
            self.time_left = self.break_duration
            print(f"Starting break phase ({self.break_duration // 60} minutes).")
        else:
            self.current_phase = "work"
            self.time_left = self.work_duration
            print(f"Starting work phase ({self.work_duration // 60} minutes).")

if __name__ == "__main__":
    pomodoro = PomodoroClock()
    print("--- CLI Pomodoro Clock ---")
    print("Commands: start, pause, reset, exit")

    while True:
        command = input("> ").lower()

        if command == "start":
            pomodoro.start()
        elif command == "pause":
            pomodoro.pause()
        elif command == "reset":
            pomodoro.reset()
        elif command == "exit":
            print("Exiting Pomodoro Clock.")
            break
        else:
            print("Unknown command.")
