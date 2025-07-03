import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(50, SCREEN_HEIGHT // 2))
        self.velocity = 0

    def flap(self):
        self.velocity = -8

    def update(self):
        self.velocity += 0.5  # Gravity
        self.rect.y += self.velocity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, height, is_top_pipe):
        super().__init__()
        self.image = pygame.Surface([50, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        if is_top_pipe:
            self.rect.bottomleft = (x, height)
        else:
            self.rect.topleft = (x, SCREEN_HEIGHT - height)

    def update(self):
        self.rect.x -= 3  # Move pipes to the left

class Game:
    def __init__(self):
        self.bird = Bird()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bird)
        self.pipes = pygame.sprite.Group()
        self.score = 0
        self.game_over = False
        self.spawn_pipe_timer = 0

    def _spawn_pipes(self):
        pipe_gap = 150
        min_pipe_height = 50
        max_pipe_height = SCREEN_HEIGHT - pipe_gap - min_pipe_height
        top_pipe_height = random.randint(min_pipe_height, max_pipe_height)
        bottom_pipe_height = SCREEN_HEIGHT - top_pipe_height - pipe_gap

        top_pipe = Pipe(SCREEN_WIDTH, top_pipe_height, True)
        bottom_pipe = Pipe(SCREEN_WIDTH, bottom_pipe_height, False)

        self.pipes.add(top_pipe)
        self.pipes.add(bottom_pipe)
        self.all_sprites.add(top_pipe)
        self.all_sprites.add(bottom_pipe)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.game_over:
                self.bird.flap()

    def update(self):
        if self.game_over:
            return

        self.all_sprites.update()

        # Spawn pipes
        self.spawn_pipe_timer += 1
        if self.spawn_pipe_timer % 90 == 0:
            self._spawn_pipes()

        # Remove off-screen pipes
        for pipe in list(self.pipes):
            if pipe.rect.right < 0:
                self.pipes.remove(pipe)
                self.all_sprites.remove(pipe)
                self.score += 0.5 # Score for passing a pipe pair

        # Collision detection
        if pygame.sprite.spritecollideany(self.bird, self.pipes) or \
           self.bird.rect.top <= 0 or self.bird.rect.bottom >= SCREEN_HEIGHT:
            self.game_over = True

    def draw(self):
        SCREEN.fill(BLACK)
        self.all_sprites.draw(SCREEN)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {int(self.score)}", True, WHITE)
        SCREEN.blit(text, (10, 10))

        if self.game_over:
            game_over_text = font.render("GAME OVER!", True, WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            SCREEN.blit(game_over_text, text_rect)

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                self.handle_input(event)

            self.update()
            self.draw()
            clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
