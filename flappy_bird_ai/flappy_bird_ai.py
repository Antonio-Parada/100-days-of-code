import os
import time
import random

class FlappyBirdGame:
    def __init__(self, width=40, height=15):
        self.width = width
        self.height = height
        self.bird_x = 5
        self.bird_y = height // 2
        self.bird_velocity = 0
        self.gravity = 1
        self.flap_strength = -2
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.pipe_gap = 5
        self.pipe_frequency = 15 # How often new pipes appear
        self.frame_count = 0

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_board(self):
        self._clear_screen()
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw bird
        if 0 <= self.bird_y < self.height:
            board[self.bird_y][self.bird_x] = '>'

        # Draw pipes
        for pipe_x, pipe_gap_y in self.pipes:
            for y in range(self.height):
                if not (pipe_gap_y <= y < pipe_gap_y + self.pipe_gap):
                    if 0 <= pipe_x < self.width:
                        board[y][pipe_x] = '#'

        print("Score: ", self.score)
        for row in board:
            print(''.join(row))
        print('-' * self.width)

    def _update_bird(self):
        self.bird_velocity += self.gravity
        self.bird_y += self.bird_velocity

        # Check ground/ceiling collision
        if self.bird_y >= self.height or self.bird_y < 0:
            self.game_over = True

    def _update_pipes(self):
        # Move pipes
        for i in range(len(self.pipes)):
            self.pipes[i][0] -= 1

        # Remove off-screen pipes
        self.pipes = [pipe for pipe in self.pipes if pipe[0] >= 0]

        # Generate new pipes
        self.frame_count += 1
        if self.frame_count % self.pipe_frequency == 0:
            pipe_gap_y = random.randint(1, self.height - self.pipe_gap - 1)
            self.pipes.append([self.width - 1, pipe_gap_y])

    def _check_collision(self):
        if self.game_over: # Already hit ground/ceiling
            return

        for pipe_x, pipe_gap_y in self.pipes:
            if pipe_x == self.bird_x:
                if not (pipe_gap_y <= self.bird_y < pipe_gap_y + self.pipe_gap):
                    self.game_over = True
                    return

        # Update score if passed pipe
        for pipe_x, _ in self.pipes:
            if pipe_x == self.bird_x - 1: # Bird just passed the pipe
                self.score += 1

    def flap(self):
        self.bird_velocity = self.flap_strength

    def play_game_with_ai(self):
        print("Welcome to Flappy Bird AI!")
        time.sleep(1)

        while not self.game_over:
            self._update_bird()
            self._update_pipes()
            self._check_collision()

            # Simple AI logic: flap if bird is too low
            if self.bird_y > self.height // 2 - 2: # Adjust this threshold as needed
                self.flap()

            self._draw_board()
            time.sleep(0.1) # Game speed

        print("Game Over! Final Score: ", self.score)

if __name__ == '__main__':
    game = FlappyBirdGame()
    game.play_game_with_ai()
