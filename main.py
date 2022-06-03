import pygame

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

WHITE = (255, 255, 255)

# Main Function
def main():
    run = True
    
    while run:
        #Check for pygame events
        for event in pygame.event.get():
        
            # Check if game is quit
            if event.type == pygame.QUIT:
                run = False
        
        WINDOW.fill(WHITE)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()

