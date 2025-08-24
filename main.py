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
    pygame.display.set_caption('Boats and Bombs!')

    # Objects
    square = sq.Sq(50, 50)

    boatimage = pygame.image.load("/home/yoichann/boats-and-bombs/boat.png").convert()
    boatimage.set_colorkey((0,255,0))


    # Game Loop
    x = 0
    y = 0
    boat_w = boatimage.get_width()
    boat_h = boatimage.get_height()
    total_speed = constants.BOAT_SPEED
    is_boosted = False
    
    running = True
    while running:

        screen.fill((0, 102, 204))

        boat = pygame.draw.rect(screen, (125, 122, 133), [x, y, boat_w, boat_h], 1)

        town = pygame.draw.rect(screen, (204, 102, 0), [530, 370, 50, 50], 0)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        if boat.colliderect(town):
            print('boat has entered town!')
            town = pygame.draw.rect(screen, (204, 204, 0), [530, 370, 50, 50], 0)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            x += total_speed
            print(f"boat is at: {x} {y}") 
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            x -= total_speed
            print(f"boat is at: {x} {y}")
        elif pygame.key.get_pressed()[pygame.K_UP]:
            y -= total_speed
            print(f"boat is at: {x} {y}") 
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            y += total_speed        
            print(f"boat is at: {x} {y}")




        # Draw Sq
        screen.blit(boatimage, (x, y))




        # Display Flip
        #print(f"boat is at: {x} {y}")
        pygame.display.update()
        


        # Clock 
        dt = clock.tick(constants.FRAMERATE) / 1000
        #print("Delta: " + dt)


if __name__ == "__main__":
    main()
