import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong with AI")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 5
AI_PADDLE_SPEED = 4 # AI is slightly slower

# Ball properties
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Game objects
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

# Score
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player 1 (Human) Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED

    # AI Paddle movement (Player 2)
    if ball.centery < paddle2.centery and paddle2.top > 0:
        paddle2.y -= AI_PADDLE_SPEED
    elif ball.centery > paddle2.centery and paddle2.bottom < HEIGHT:
        paddle2.y += AI_PADDLE_SPEED

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1

    # Ball out of bounds (scoring)
    if ball.left <= 0:
        player2_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1 # Reset ball direction
    elif ball.right >= WIDTH:
        player1_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1 # Reset ball direction

    # Drawing
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, paddle1)
    pygame.draw.rect(SCREEN, WHITE, paddle2)
    pygame.draw.ellipse(SCREEN, WHITE, ball)

    # Display score
    text_surface = font.render(f"{player1_score} - {player2_score}", True, WHITE)
    SCREEN.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 10))

    # Update display
    pygame.display.flip()

    # Cap frame rate
    clock.tick(60)

pygame.quit()
