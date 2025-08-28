import pygame, sys

import player, constants, boat



def main():
    print("Hello from boats-n-bombs!!!")

    # Initialize PyGame
    pygame.init()

    # Clock
    clock = pygame.time.Clock()
    dt = 0

    # Screenpas
    screen = pygame.display.set_mode((constants.SCREEN_W, constants.SCREEN_H), pygame.FULLSCREEN)
    pygame.display.set_caption('Boats and Bombs!')

    # Objects
    player_boat = boat.Boat('Player Boat', "/home/yoichann/boats-and-bombs/boat.png", (0, 0))
    p1 = player.Player('Bingus', player_boat)


    # Fonts
    mapfont = pygame.font.SysFont('Serif', 32)
    textsurface = pygame.font.Font.render(mapfont, str(screen.get_width()), True, (128, 128, 128))

    # Game Loop
    
    running = True
    while running:

        screen.fill((0, 102, 204))

        p1.boat.draw(screen)

        town = pygame.draw.rect(screen, (204, 102, 0), [530, 370, 50, 50], 0)


        screen.blit(textsurface, (333, 444))


        # PyGame EXIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            sys.exit()



        # Collision Test
        if p1.boat.hitbox.colliderect(town):
            print('boat has entered town!')
            town = pygame.draw.rect(screen, (204, 204, 0), [530, 370, 50, 50], 0)
            ui = pygame.draw.rect(screen, (35, 35, 35), [0, 0, screen.get_width(), 200], 0) 






        # Draw Sq
        textsurface = pygame.font.Font.render(mapfont, str(f"X: {p1.boat.pos_x}, Y: {p1.boat.pos_y}"), True, (128, 128, 128))




        # Display Flip
        #print(f"boat is at: {x} {y}")
        pygame.display.update()
        


        # Clock 
        dt = clock.tick(constants.FRAMERATE) / 1000
        #print("Delta: " + dt)


if __name__ == "__main__":
    main()
