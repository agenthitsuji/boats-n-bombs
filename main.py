import pygame, sys

import player, sq, constants



def main():
    print("Hello from boats-n-bombs!!!")

    # Initialize PyGame
    pygame.init()

    # Clock
    clock = pygame.time.Clock()
    dt = 0

    # Screen
    screen = pygame.display.set_mode((constants.SCREEN_W, constants.SCREEN_H))
    pygame.display.set_caption('Hello pets!')

    # Objects
    square = sq.Sq(50, 50)

    # Game Loop
    x = 0
    y = 0
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            x += 3
            print(f"boat is at: {x} {y}") 
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x -= 3
            print(f"boat is at: {x} {y}")
        if pygame.key.get_pressed()[pygame.K_UP]:
            y += 3
            print(f"boat is at: {x} {y}") 
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            y -= 3        
            print(f"boat is at: {x} {y}")

        # Draw Sq
        #screen.blit(square.surf, (200, 200))

        boat = pygame.draw.rect(screen, (125, 122, 133), [x, y, 60, 40], 4)


        # Display Flip
        #print(f"boat is at: {x} {y}")
        pygame.display.update()
        


        # Clock 
        dt = clock.tick(constants.FRAMERATE) / 1000
        #print("Delta: " + dt)


if __name__ == "__main__":
    main()
