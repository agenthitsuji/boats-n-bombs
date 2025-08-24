import pygame, sys
import sq



def main():
    print("Hello from tournament-of-fighters!")

    # Initialize PyGame
    pygame.init()

    # Clock
    clock = pygame.time.Clock()
    dt = 0

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
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        # Draw square
        screen.blit(square.surf, (200, 200))


        # Display Flip
        pygame.display.flip()

        # Clock 
        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()
