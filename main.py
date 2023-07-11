"""
This is a game with "Space invaders" theme.
"""

import random
import math
import pygame

# Initialize pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))

# Title, icon and background
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.jpg")

# Player variables
player_img = pygame.image.load("spaceship.png")
player_x = 368
player_y = 536
player_x_change = 0

# Enemy variables
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 5

for i in range(number_of_enemies):
    enemy_img.append(pygame.image.load("alien.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(30, 200))
    enemy_x_change.append(0.3)
    enemy_y_change.append(30)

# Bullet variables
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 536
bullet_x_change = 0
bullet_y_change = 1
bullet_visible = False

# Score variable
score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)
score_text_x = 10
score_text_y = 10

# Game over text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

# Game over function
def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 200))

# Show score on screen
def show_score(x, y):
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (x, y))

# Show player on screen
def player(x, y):
    screen.blit(player_img, (x, y))

# Show enemy on screen
def enemy(x, y, enemy_index):
    screen.blit(enemy_img[enemy_index], (x, y))

# Show bullet on screen
def shoot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img, (x + 16, y + 10))

# Detect collision
def detect_collision(x_1, y_1, x_2, y_2):
    x_sub = x_1 - x_2
    y_sub = y_1 - y_2
    distance = math.sqrt(math.pow(x_sub, 2) + math.pow(y_sub, 2))
    if distance < 27:
        return True
    else:
        return False

# Game loop
is_running = True
while is_running:

    # Image background
    screen.blit(background, (0, 0))

    # Fill the screen with blue
    # screen.fill((0, 0, 255))

    # player_x += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            # Move player left or right and shoot bullet
            if event.key == pygame.K_LEFT: # If left arrow key is pressed
                # print("Left arrow key was pressed")
                player_x_change -= 0.7
            if event.key == pygame.K_SPACE: # If space bar is pressed
                if not bullet_visible:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)
            if event.key == pygame.K_RIGHT: # If right arrow key is pressed
                # print("Right arrow key was pressed")
                player_x_change += 0.7
        if event.type == pygame.KEYUP: # If key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Keystroke has been released")
                player_x_change = 0

    # Update player position
    player_x += player_x_change

    # Set boundaries for player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Loop through enemies
    for i in range (number_of_enemies):
        # Detect game over
        if enemy_y[i] > 500:
            for j in range(number_of_enemies):
                enemy_y[j] = 1000
            game_over_text()
            break

        # Update enemy position
        enemy_x[i] += enemy_x_change[i]

        # Set boundaries for enemy
        if enemy_x[i] <= 0:
            enemy_x_change[i] += 0.3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] -= 0.3
            enemy_y[i] += enemy_y_change[i]

        # Detect collision
        collision = detect_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(30, 200)
            bullet_visible = False
            score += 1
            bullet_y = 500

        # Show enemy on screen
        enemy(enemy_x[i], enemy_y[i], i)

    # Shoot bullet
    if bullet_y <= -64:
        bullet_y = 500
        bullet_visible = False
    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Show player on screen
    player(player_x, player_y)

    # Show score on screen
    show_score(score_text_x, score_text_y)

    # Update the screen
    pygame.display.update()
