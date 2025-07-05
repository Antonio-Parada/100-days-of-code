import pygame
import random

class FlappyBird:
    def __init__(self):
        self.screen_width = 288
        self.screen_height = 512
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Flappy Bird AI')
        self.clock = pygame.time.Clock()

        self.bird_x = 50
        self.bird_y = self.screen_height // 2
        self.bird_y_velocity = 0

        self.pipe_width = 52
        self.pipe_height = 320
        self.pipe_gap = 100
        self.pipes = []
        self.pipe_spawn_timer = 0

        self.score = 0
        self.game_over = False

    def spawn_pipe(self):
        pipe_y = random.randint(self.pipe_gap // 2, self.screen_height - self.pipe_gap // 2)
        self.pipes.append(pygame.Rect(self.screen_width, 0, self.pipe_width, pipe_y - self.pipe_gap // 2))
        self.pipes.append(pygame.Rect(self.screen_width, pipe_y + self.pipe_gap // 2, self.pipe_width, self.screen_height - (pipe_y + self.pipe_gap // 2)))

    def update(self, action):
        if not self.game_over:
            if action:
                self.bird_y_velocity = -9

            self.bird_y_velocity += 1
            self.bird_y += self.bird_y_velocity

            self.pipe_spawn_timer += 1
            if self.pipe_spawn_timer > 90:
                self.spawn_pipe()
                self.pipe_spawn_timer = 0

            for pipe in self.pipes:
                pipe.x -= 3

            self.pipes = [pipe for pipe in self.pipes if pipe.right > 0]

            bird_rect = pygame.Rect(self.bird_x, self.bird_y, 34, 24)
            for pipe in self.pipes:
                if bird_rect.colliderect(pipe):
                    self.game_over = True

            if self.bird_y > self.screen_height or self.bird_y < 0:
                self.game_over = True

            if len(self.pipes) > 0 and self.pipes[0].right < self.bird_x and not self.pipes[0].colliderect(bird_rect):
                self.score += 1

    def draw(self):
        self.screen.fill((78, 192, 202))
        for pipe in self.pipes:
            pygame.draw.rect(self.screen, (0, 255, 0), pipe)
        pygame.draw.rect(self.screen, (255, 255, 0), (self.bird_x, self.bird_y, 34, 24))
        pygame.display.flip()

    def step(self, action):
        self.update(action)
        self.draw()
        self.clock.tick(30)
        return self.score, self.game_over
