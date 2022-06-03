import os

import pygame

WIDTH, HEIGHT = 900, 500  # WINDOW RESOLUTION
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # SET WINDOW RESOLUTION
pygame.display.set_caption("Space Shooter")  # SET WINDOW TITLE

WHITE = (255, 255, 255)  # RGB Code for White
FPS = 60  # Game FPS
SHIP_IMG_WIDTH, SHIP_IMG_HEIGHT = 55, 40  # Dimensions for Spaceship Sprites

BLUE_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'shipBlue.png'))  # IMPORT BLUE SPACESHIP IMAGE
GREEN_SHIP_IMG = pygame.image.load(os.path.join('Assets', 'shipGreen.png'))  # IMPORT GREEN SPACESHIP IMAGE

BLUE_SHIP = pygame.transform.scale(BLUE_SHIP_IMG, (SHIP_IMG_WIDTH, SHIP_IMG_HEIGHT))  # RESCALE BLUE SPACESHIP IMAGE
GREEN_SHIP = pygame.transform.scale(GREEN_SHIP_IMG, (SHIP_IMG_WIDTH, SHIP_IMG_HEIGHT))  # RESCALE GREEN SPACESHIP IMAGE


def draw_window():
    WINDOW.fill(WHITE)  # Fill Screen With White Color
    WINDOW.blit(BLUE_SHIP, (250, 675))  # Used to show Green Spaceship on screen
    WINDOW.blit(GREEN_SHIP, (0, 225))  # Used to show Blue Spaceship on screen
    pygame.display.update()  # Update Screen


# Main Function
def main():
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

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
