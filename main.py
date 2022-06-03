import os

import pygame

WIDTH, HEIGHT = 900, 500  # WINDOW RESOLUTION
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # SET WINDOW RESOLUTION
pygame.display.set_caption("Space Shooter")  # SET WINDOW TITLE

WHITE = (255, 255, 255)  # RGB Code for White
BLACK = (0, 0, 0)  # RGB Code for Black

BORDER = pygame.Rect((WIDTH / 2) - 5, 0, 10, HEIGHT)

FPS = 60  # Game FPS
VELOCITY = 5
BULLET_VELOCITY = 7
MAX_NUM_OF_BULLETS = 5
SHIP_WIDTH, SHIP_HEIGHT = 55, 40  # Dimensions for Spaceship Sprites
BULLET_WIDTH, BULLET_HEIGHT = 10, 5

GREEN_SHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'shipGreen.png')),
                                         270)  # IMPORT GREEN SPACESHIP IMAGE
BLUE_SHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'shipBlue.png')),
                                        90)  # IMPORT BLUE SPACESHIP IMAGE
GREEN_BULLET_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'laserGreen.png')),
                                           90)  # IMPORT GREEN SPACESHIP IMAGE
BLUE_BULLET_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'laserBlue.png')),
                                          270)  # IMPORT BLUE SPACESHIP IMAGE

GREEN_SHIP = pygame.transform.scale(GREEN_SHIP_IMG, (SHIP_WIDTH, SHIP_HEIGHT))  # RESCALE GREEN SPACESHIP IMAGE
BLUE_SHIP = pygame.transform.scale(BLUE_SHIP_IMG, (SHIP_WIDTH, SHIP_HEIGHT))  # RESCALE BLUE SPACESHIP IMAGE
GREEN_BULLET = pygame.transform.scale(GREEN_BULLET_IMG, (BULLET_WIDTH, BULLET_HEIGHT))
BLUE_BULLET = pygame.transform.scale(BLUE_BULLET_IMG, (BULLET_WIDTH, BULLET_HEIGHT))


def draw_window(green, blue):
    WINDOW.fill(WHITE)  # Fill Screen With White Color
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    WINDOW.blit(GREEN_SHIP, (green.x, green.y))  # Used to show Green Spaceship on screen
    WINDOW.blit(BLUE_SHIP, (blue.x, blue.y))  # Used to show Blue Spaceship on screen
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


# Main Function
def main():
    green = pygame.Rect(100, 300, SHIP_WIDTH, SHIP_HEIGHT)
    blue = pygame.Rect(700, 300, SHIP_WIDTH, SHIP_HEIGHT)
    green_bullet = pygame.Rect(green.x + green.width, green.y + green.height / 2 - 2, 10, 5)
    blue_bullet = pygame.Rect(blue.x, blue.y + blue.height / 2 - 2, 10, 5)

    green_bullets = []
    blue_bullets = []

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(green_bullets) < MAX_NUM_OF_BULLETS:
                    green_bullets.append(green_bullet)
                if event.key == pygame.K_RCTRL and len(blue_bullets) < MAX_NUM_OF_BULLETS:
                    blue_bullets.append(blue_bullet)

        keys_pressed = pygame.key.get_pressed()
        green_movement_handler(keys_pressed, green)
        blue_movement_handler(keys_pressed, blue)

        draw_window(green, blue)

    pygame.quit()


if __name__ == "__main__":
    main()
