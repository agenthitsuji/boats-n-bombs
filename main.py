import pygame
import sq



def main():
    print("Hello from tournament-of-fighters!")

    # Initialize PyGame
    pygame.init()

    # Screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hello pets!')

    # Objects
    square = sq.Sq(50, 50)
    print(square)

    # Game Lopp
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                running = False

    # Draw square
    screen.blit(square.surf, (200, 200))

    pygame.display.flip()


if __name__ == "__main__":
    main()
