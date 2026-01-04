import pygame
import random
import sys

pygame.init()

# WINDOW
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("|GAME|")


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# COLORS
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# PLAYER
player_size = 50
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 6
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

# ENEMIES
enemy_size = 50
enemy_count = 2
enemy_speed = 6
speed_increase_timer = 0

enemies = []
for _ in range(enemy_count):
    enemies.append({
        "rect": pygame.Rect(
            random.randint(0, WIDTH - enemy_size),
            random.randint(0, HEIGHT - enemy_size),
            enemy_size,
            enemy_size
        ),
        "dx": random.choice([-1, 1]),
        "dy": random.choice([-1, 1])
    })

# SCORE
score = 0
start_time = pygame.time.get_ticks()

# GAME LOOP
running = True
while running:
    dt = clock.tick(60)
    screen.fill(WHITE)

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # PLAYER MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # KEEP PLAYER INSIDE SCREEN
    player_rect.x = max(0, min(player_rect.x, WIDTH - player_size))
    player_rect.y = max(0, min(player_rect.y, HEIGHT - player_size))

    # ENEMY MOVEMENT
    for enemy in enemies:
        enemy["rect"].x += enemy["dx"] * enemy_speed
        enemy["rect"].y += enemy["dy"] * enemy_speed

        # BOUNCE FROM WALLS
        if enemy["rect"].left <= 0 or enemy["rect"].right >= WIDTH:
            enemy["dx"] *= -1
        if enemy["rect"].top <= 0 or enemy["rect"].bottom >= HEIGHT:
            enemy["dy"] *= -1

        # COLLISION DETECTION
        if player_rect.colliderect(enemy["rect"]):
            game_over_text = font.render("GAME OVER", True, RED)
            screen.blit(game_over_text, (WIDTH//2 - 90, HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    # INCREASE ENEMY SPEED OVER TIME
    speed_increase_timer += dt
    if speed_increase_timer >= 5000:  # every 5 seconds
        enemy_speed += 1
        speed_increase_timer = 0

    # SCORE (time survived)
    score = (pygame.time.get_ticks() - start_time) // 1000
    score_text = font.render(f"Score: {score}", True, BLACK)

    # DRAW EVERYTHING
    pygame.draw.rect(screen, BLUE, player_rect)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy["rect"])

    screen.blit(score_text, (10, 10))
    clock.tick(60)

    pygame.display.flip()











