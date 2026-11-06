
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colours
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 60, 60)
BLACK = (0, 0, 0)
GREEN = (30, 160, 70)

# Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 60) 

# Basket settings
basket_width = 80
basket_height = 20
basket_x = 210
basket_y = 560
basket_speed = 10

# Falling object settings
object_size = 20
object_x = random.randint(0, WIDTH - object_size)
object_y = 0
object_speed = 5

# Score and lives
score = 0
lives = 3

# Game settings
clock = pygame.time.Clock()
running = True
game_over = False

# Main game loop
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Restart after Game Over
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                score = 0
                lives = 3
                basket_x = 210
                object_x = random.randint(0, WIDTH - object_size)
                object_y = 0
                object_speed = 5
                game_over = False

    if not game_over:

        # Move basket
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed

        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed

        # Keep basket inside the screen
        basket_x = max(
            0, min(basket_x, WIDTH - basket_width)
        )

        # Move falling object
        object_y += object_speed

        # Create rectangles for collision detection
        basket_rect = pygame.Rect(
            basket_x, basket_y,
            basket_width, basket_height
        )

        object_rect = pygame.Rect(
            object_x, object_y,
            object_size, object_size
        )

        # Catch the object
        if basket_rect.colliderect(object_rect):
            score += 1
            object_y = 0
            object_x = random.randint(0, WIDTH - object_size)

            # Increase difficulty gradually
            object_speed = min(12, 5 + score // 5)

        # Miss the object
        if object_y > HEIGHT:
            lives -= 1
            object_y = 0
            object_x = random.randint(0, WIDTH - object_size)

            if lives <= 0:
                game_over = True

    # Draw background
    screen.fill(WHITE)

    if not game_over:

        # Draw basket
        pygame.draw.rect(
            screen, BLUE,
            (basket_x, basket_y,
             basket_width, basket_height)
        )

        # Draw falling object
        pygame.draw.rect(
            screen, RED,
            (object_x, object_y,
             object_size, object_size)
        )

        # Display score
        score_text = font.render(
            f"Score: {score}", True, BLACK
        )
        screen.blit(score_text, (10, 10))

        # Display lives
        lives_text = font.render(
            f"Lives: {lives}", True, GREEN
        )
        screen.blit(lives_text, (370, 10))

    else:

        # Game Over screen
        title = big_font.render(
            "GAME OVER", True, RED
        )
        final_score = font.render(
            f"Final Score: {score}", True, BLACK
        )
        restart_text = font.render(
            "Press R to Restart", True, BLUE
        )
        quit_text = font.render(
            "Close window to Quit", True, BLACK
        )

        screen.blit(
            title,
            title.get_rect(center=(WIDTH // 2, 230))
        )
        screen.blit(
            final_score,
            final_score.get_rect(center=(WIDTH // 2, 300))
        )
        screen.blit(
            restart_text,
            restart_text.get_rect(center=(WIDTH // 2, 370))
        )
        screen.blit(
            quit_text,
            quit_text.get_rect(center=(WIDTH // 2, 420))
        )

    # Update display
    pygame.display.update()

    # Limit game to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()



