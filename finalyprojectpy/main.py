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
enemy_speed = 0.2

for i in range(number_of_enemies):
    enemy_img.append(pygame.image.load("alien.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(30, 200))
    enemy_x_change.append(enemy_speed)
    enemy_y_change.append(30)

# Meteorite variables
meteorite_img = []
meteorite_x = []
meteorite_y = []
meteorite_x_change = []
meteorite_y_change = []
meteorite_visible = False
number_of_meteorites = 3

for i in range(number_of_meteorites):
    meteorite_img.append(pygame.image.load("meteorite.png"))
    meteorite_x.append(random.randint(0, 736))
    meteorite_y.append(random.randint(0, 200))
    meteorite_x_change.append(0)
    meteorite_y_change.append(0.1)

# Bullet variables
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 536
bullet_x_change = 0
bullet_y_change = 2
bullet_visible = False

# Score variable
score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)
score_text_x = 10
score_text_y = 10

# Game over text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

# Game state
game_state = "menu"

# Player name
player_name = ""

# New variable
is_returning = False


# Show menu
def show_menu():
    menu_font = pygame.font.Font("freesansbold.ttf", 64)
    title_text = menu_font.render("Space Invaders", True, (255, 255, 255))
    start_text = score_font.render("1. Iniciar juego", True, (255, 255, 255))
    scoreboard_text = score_font.render("2. Ver scoreboard", True, (255, 255, 255))
    credits_text = score_font.render("3. Créditos", True, (255, 255, 255))
    screen.blit(title_text, (200, 200))
    screen.blit(start_text, (300, 300))
    screen.blit(scoreboard_text, (300, 350))
    screen.blit(credits_text, (300, 400))


# Show game over text
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


# Show meteorite on screen
def meteorite(x, y, meteorite_index):
    global meteorite_visible
    meteorite_visible = False
    screen.blit(meteorite_img[meteorite_index], (x, y))


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


# Save score to file
def save_score(name, score):
    with open("scoreboard.txt", "a") as file:
        file.write(f"{name}: {score}\n")


# Show name input screen
def show_name_input():
    screen.fill((0, 0, 0))
    input_font = pygame.font.Font("freesansbold.ttf", 32)
    input_text = input_font.render("What is your name:", True, (255, 255, 255))
    screen.blit(input_text, (250, 250))


# Show player name on screen
def show_player_name():
    name_font = pygame.font.Font("freesansbold.ttf", 32)
    name_text = name_font.render(f"Name: {player_name}", True, (255, 255, 255))
    screen.blit(name_text, (10, 10))


# Reset game variables
def reset_game():
    global player_x, player_y, player_x_change
    global enemy_x, enemy_y, enemy_x_change, enemy_y_change
    global meteorite_x, meteorite_y, meteorite_x_change, meteorite_y_change
    global bullet_x, bullet_y, bullet_x_change, bullet_y_change, bullet_visible
    global score, player_name, is_returning

    player_x = 368
    player_y = 536
    player_x_change = 0

    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []
    for i in range(number_of_enemies):
        enemy_x.append(random.randint(0, 736))
        enemy_y.append(random.randint(30, 200))
        enemy_x_change.append(enemy_speed)
        enemy_y_change.append(30)

    meteorite_x = []
    meteorite_y = []
    meteorite_x_change = []
    meteorite_y_change = []
    meteorite_visible = False
    for i in range(number_of_meteorites):
        meteorite_x.append(random.randint(0, 736))
        meteorite_y.append(random.randint(0, 200))
        meteorite_x_change.append(0)
        meteorite_y_change.append(0.1)

    bullet_x = 0
    bullet_y = 536
    bullet_x_change = 0
    bullet_y_change = 2
    bullet_visible = False

    score = 0
    player_name = ""
    is_returning = False


# Reset game and go back to menu
def return_to_menu():
    reset_game()
    global game_state
    game_state = "menu"


# Game loop
is_running = True
is_name_input = True
while is_running:
    if is_name_input:
        show_name_input()
        show_player_name()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_name_input = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

    else:
        # Image background
        screen.blit(background, (0, 0))

        if game_state == "menu":
            show_menu()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        reset_game()
                        game_state = "playing"
                    elif event.key == pygame.K_2:
                        game_state = "scoreboard"
                    elif event.key == pygame.K_3:
                        game_state = "credits"
                    elif event.key == pygame.K_4:
                        return_to_menu()

        elif game_state == "over":
            save_score(player_name, score)
            game_state = "menu"

        elif game_state == "playing":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_x_change -= 0.7
                    if event.key == pygame.K_SPACE:
                        if not bullet_visible:
                            bullet_x = player_x
                            shoot_bullet(bullet_x, bullet_y)
                    if event.key == pygame.K_RIGHT:
                        player_x_change += 0.7
                    if event.key == pygame.K_r:
                        return_to_menu()
                    if event.key == pygame.K_4:
                        return_to_menu()

                if event.type == pygame.KEYUP:  # If key is released
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_x_change = 0

            # Update player position
            player_x += player_x_change

            # Set boundaries for player
            if player_x <= 0:
                player_x = 0
            elif player_x >= 736:
                player_x = 736

            # Validate meteorite visibility
            if score >= 1:
                meteorite_visible = True

            # Loop through meteorites
            for i in range(number_of_meteorites):
                # Detect collision between meteorite and player
                collision = detect_collision(meteorite_x[i], meteorite_y[i], player_x, player_y)
                if collision:
                    game_over_text()
                    game_state = "over"
                    break

                # Detect collision between bullet and meteorite
                collision = detect_collision(meteorite_x[i], meteorite_y[i], bullet_x, bullet_y)
                if collision:
                    bullet_y = 536
                    bullet_visible = False
                    meteorite_y[i] = random.randint(0, 200)
                    meteorite_x[i] = random.randint(0, 736)

                # Update meteorite position
                if meteorite_visible:
                    meteorite_y[i] += meteorite_y_change[i]

                # Set boundaries for meteorite
                if meteorite_y[i] >= 600:
                    meteorite_y[i] = random.randint(0, 568)
                    meteorite_x[i] = random.randint(0, 736)
                    meteorite_visible = False

                # Show meteorite on screen
                if meteorite_y[i] <= 200:
                    meteorite_y[i] = random.randint(0, 200)
                    meteorite_visible = False
                if meteorite_visible:
                    meteorite(meteorite_x[i], meteorite_y[i], i)

            # Loop through enemies
            for i in range(number_of_enemies):
                # Detect game over
                if enemy_y[i] > 500:
                    for j in range(number_of_enemies):
                        enemy_y[j] = 1000
                    game_over_text()
                    game_state = "over"
                    break

                # Update enemy position
                enemy_x[i] += enemy_x_change[i]

                if 10 <= score < 20:
                    enemy_speed = 0.3
                elif score >= 20:
                    enemy_speed = 0.5

                # Set boundaries for enemy
                if enemy_x[i] <= 0:
                    enemy_x_change[i] = enemy_speed
                    enemy_y[i] += enemy_y_change[i]
                elif enemy_x[i] >= 736:
                    enemy_x_change[i] = -enemy_speed
                    enemy_y[i] += enemy_y_change[i]

                # Detect collision
                collision = detect_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
                if collision:
                    enemy_x[i] = random.randint(0, 736)
                    enemy_y[i] = random.randint(30, 200)
                    bullet_visible = False
                    score += 1
                    bullet_y = 536

                # Show enemy on screen
                enemy(enemy_x[i], enemy_y[i], i)

            # Shoot bullet
            if bullet_y <= -64:
                bullet_y = 536
                bullet_visible = False
            if bullet_visible:
                shoot_bullet(bullet_x, bullet_y)
                bullet_y -= bullet_y_change

            # Show player on screen
            player(player_x, player_y)

            # Show score on screen
            show_score(score_text_x, score_text_y)

        elif game_state == "scoreboard":
            scoreboard_font = pygame.font.Font("freesansbold.ttf", 24)
            scoreboard_text_x = 300
            scoreboard_text_y = 300

            screen.fill((0, 0, 0))
            with open("scoreboard.txt", "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    scoreboard_text = scoreboard_font.render(line.strip(), True, (255, 255, 255))
                    screen.blit(scoreboard_text, (scoreboard_text_x, scoreboard_text_y + i * 30))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_4:
                        game_state = "menu"

        elif game_state == "credits":
            credits_font = pygame.font.Font("freesansbold.ttf", 32)
            credits_text_x = 150
            credits_text_y = 300

            screen.fill((0, 0, 0))
            credits_text = credits_font.render("Created by Uriel, Santiago & Edu ", True,
                                               (0, 255, 255))
            screen.blit(credits_text, (credits_text_x, credits_text_y))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_4:
                        game_state = "menu"

        # Update the screen
        pygame.display.update()

# Quit pygame
pygame.quit()