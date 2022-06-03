import os

import pygame

WIDTH, HEIGHT = 900, 500  # WINDOW RESOLUTION
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # SET WINDOW RESOLUTION
pygame.display.set_caption("Space Shooter")  # SET WINDOW TITLE

WHITE = (255, 255, 255)  # RGB Code for White
FPS = 60  # Game FPS
VELOCITY = 5
SHIP_WIDTH, SHIP_HEIGHT = 55, 40  # Dimensions for Spaceship Sprites

GREEN_SHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'shipGreen.png')),
                                         270)  # IMPORT GREEN SPACESHIP IMAGE
BLUE_SHIP_IMG = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'shipBlue.png')),
                                        90)  # IMPORT BLUE SPACESHIP IMAGE

GREEN_SHIP = pygame.transform.scale(GREEN_SHIP_IMG, (SHIP_WIDTH, SHIP_HEIGHT))  # RESCALE GREEN SPACESHIP IMAGE
BLUE_SHIP = pygame.transform.scale(BLUE_SHIP_IMG, (SHIP_WIDTH, SHIP_HEIGHT))  # RESCALE BLUE SPACESHIP IMAGE


def draw_window(green, blue):
    WINDOW.fill(WHITE)  # Fill Screen With White Color
    WINDOW.blit(GREEN_SHIP, (green.x, green.y))  # Used to show Green Spaceship on screen
    WINDOW.blit(BLUE_SHIP, (blue.x, blue.y))  # Used to show Blue Spaceship on screen
    pygame.display.update()  # Update Screen


# HANDLE GREEN SPACESHIP MOVEMENT FROM PLAYER INPUT
def green_movement_handler(keys_pressed, green):
    if keys_pressed[pygame.K_a]:  # LEFT
        green.x -= VELOCITY
    if keys_pressed[pygame.K_d]:  # RIGHT
        green.x += VELOCITY
    if keys_pressed[pygame.K_w]:  # UP
        green.y -= VELOCITY
    if keys_pressed[pygame.K_s]:  # DOWN
        green.y += VELOCITY


# HANDLE GREEN SPACESHIP MOVEMENT FROM PLAYER INPUT
def blue_movement_handler(keys_pressed, blue):
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        blue.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        blue.x += VELOCITY
    if keys_pressed[pygame.K_UP]:  # UP
        blue.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        blue.y += VELOCITY


# Main Function
def main():
    green = pygame.Rect(100, 300, SHIP_WIDTH, SHIP_HEIGHT)
    blue = pygame.Rect(700, 300, SHIP_WIDTH, SHIP_HEIGHT)

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

        keys_pressed = pygame.key.get_pressed()
        green_movement_handler(keys_pressed, green)
        blue_movement_handler(keys_pressed, blue)

        draw_window(green, blue)

    pygame.quit()


if __name__ == "__main__":
    main()
