import os
import pygame
pygame.font.init() # Initialise pygame fonts


WIDTH, HEIGHT = 900, 500  # WINDOW RESOLUTION
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # SET WINDOW RESOLUTION
pygame.display.set_caption("Space Shooter")  # SET WINDOW TITLE

WHITE = (255, 255, 255)  # RGB Code for White
BLACK = (0, 0, 0)  # RGB Code for Black
GREEN = (110, 194, 54)  # RGB Code for Green Bullet
BLUE = (53, 180, 235)  # RGB Code for Blue Bullet

BORDER = pygame.Rect((WIDTH // 2) - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('kenvector_future', 40)
WINNER_FONT = pygame.font.SysFont('kenvector_future', 100)

FPS = 60  # Game FPS
VELOCITY = 5  # Speed of Spaceship
BULLET_VELOCITY = 7  # Speed of Bullets
MAX_NUM_OF_BULLETS = 5  # Max Number of Bullets available on screen at once
SHIP_WIDTH, SHIP_HEIGHT = 55, 40  # Dimensions for Spaceship Sprites
BULLET_WIDTH, BULLET_HEIGHT = 10, 5  # Dimensions for bullets

GREEN_HIT = pygame.USEREVENT + 1
BLUE_HIT = pygame.USEREVENT + 2

GREEN_SHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'shipGreen.png')),
                                         270)  # IMPORT GREEN SPACESHIP IMAGE
BLUE_SHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'shipBlue.png')),
                                        90)  # IMPORT BLUE SPACESHIP IMAGE

GREEN_SHIP = pygame.transform.scale(GREEN_SHIP_IMG, (SHIP_WIDTH, SHIP_HEIGHT))  # RESCALE GREEN SPACESHIP IMAGE
BLUE_SHIP = pygame.transform.scale(BLUE_SHIP_IMG, (SHIP_WIDTH, SHIP_HEIGHT))  # RESCALE BLUE SPACESHIP IMAGE

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))


def draw_window(green, blue, green_bullets, blue_bullets, green_health, blue_health):
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)

    green_health_text = HEALTH_FONT.render("Health: " + str(green_health), 1, WHITE)
    blue_health_text = HEALTH_FONT.render("Health: " + str(blue_health), 1, WHITE)
    WINDOW.blit(green_health_text, (WIDTH-green_health_text.get_width() - 10, 10))
    WINDOW.blit(blue_health_text, (10, 10))

    WINDOW.blit(GREEN_SHIP, (green.x, green.y))  # Used to show Green Spaceship on screen
    WINDOW.blit(BLUE_SHIP, (blue.x, blue.y))  # Used to show Blue Spaceship on screen



    for bullet in green_bullets:
        pygame.draw.rect(WINDOW, GREEN, bullet)
    for bullet in blue_bullets:
        pygame.draw.rect(WINDOW, BLUE, bullet)

    pygame.display.update()  # Update Screen


# HANDLE GREEN SPACESHIP MOVEMENT FROM PLAYER INPUT
def green_movement_handler(keys_pressed, green):
    if keys_pressed[pygame.K_a] and green.x - VELOCITY > -5:  # LEFT
        green.x -= VELOCITY
    if keys_pressed[pygame.K_d] and green.x - VELOCITY + green.width < BORDER.x - 5:  # RIGHT
        green.x += VELOCITY
    if keys_pressed[pygame.K_w] and green.y - VELOCITY > 0:  # UP
        green.y -= VELOCITY
    if keys_pressed[pygame.K_s] and green.y - VELOCITY + green.height < HEIGHT - 5:  # DOWN
        green.y += VELOCITY


# HANDLE GREEN SPACESHIP MOVEMENT FROM PLAYER INPUT
def blue_movement_handler(keys_pressed, blue):
    if keys_pressed[pygame.K_LEFT] and blue.x - VELOCITY > BORDER.x + BORDER.width - 5:  # LEFT
        blue.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY + blue.width < WIDTH - 5:  # RIGHT
        blue.x += VELOCITY
    if keys_pressed[pygame.K_UP] and blue.y - VELOCITY > 0:  # UP
        blue.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and blue.y - VELOCITY + blue.height < HEIGHT - 5:  # DOWN
        blue.y += VELOCITY


def handle_bullets(green_bullets, blue_bullets, green, blue):
    for bullet in green_bullets:
        bullet.x += BULLET_VELOCITY
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            green_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            green_bullets.remove(bullet)

    for bullet in blue_bullets:
        bullet.x -= BULLET_VELOCITY
        if green.colliderect(bullet):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            blue_bullets.remove(bullet)
        elif bullet.x < 0:
            blue_bullets.remove(bullet)

def draw_winner (text):
    winner_text = WINNER_FONT.render(text, 1, WHITE)
    WINDOW.blit(winner_text, (WIDTH//2 - winner_text.get_width()/2, HEIGHT//2 - winner_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# Main Function
def main():
    green = pygame.Rect(100, 300, SHIP_WIDTH, SHIP_HEIGHT)
    blue = pygame.Rect(700, 300, SHIP_WIDTH, SHIP_HEIGHT)

    green_bullets = []
    blue_bullets = []

    green_health = 10
    blue_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        # Ensure Game Runs at 60FPS
        clock.tick(FPS)
        # Check for pygame events
        for event in pygame.event.get():

            # Check if game is quit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(green_bullets) < MAX_NUM_OF_BULLETS:
                    bullet = pygame.Rect(green.x + green.width, green.y + green.height // 2 - 2, 10, 5)
                    green_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(blue_bullets) < MAX_NUM_OF_BULLETS:
                    bullet = pygame.Rect(blue.x, blue.y + blue.height // 2 - 2, 10, 5)
                    blue_bullets.append(bullet)

            if event.type == GREEN_HIT:
                blue_health -= 1

            if event.type == BLUE_HIT:
                green_health -= 1

        winner_text = ""
        if green_health < 0:
            winner_text = "Green Wins"

        if blue_health < 0:
            winner_text = "Blue Wins"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        green_movement_handler(keys_pressed, green)
        blue_movement_handler(keys_pressed, blue)

        handle_bullets(green_bullets, blue_bullets, green, blue)

        draw_window(green, blue, green_bullets, blue_bullets, green_health, blue_health)

    main()


if __name__ == "__main__":
    main()
