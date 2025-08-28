import pygame, sys, constants

from town import Town
from player import Player
from boat import Boat




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
    player_boat = Boat('Player Boat', "/home/yoichann/boats-and-bombs/boat.png", (0, 0))
    p1 = Player('Bingus', player_boat)
    town = Town('Walterville', 3, 350, 220)

    # Drawing Table
    drawable = [player_boat, town]

    # Fonts
    mapfont = pygame.font.SysFont('Serif', 32)
    textsurface = pygame.font.Font.render(mapfont, str(screen.get_width()), True, (128, 128, 128))

    # Game Loop
    
    running = True

    while running:

        screen.fill((0, 102, 204))

        for item in drawable:
            item.draw(screen)

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
        if p1.boat.hitbox.colliderect(town.hitbox):
            print('boat has entered town!')
            p1.boat.supply += town.supply_bonus
            ui = pygame.draw.rect(screen, (35, 35, 35), [0, 0, screen.get_width(), 200], 0) 






        # Draw Sq
        textsurface = pygame.font.Font.render(mapfont, str(f"X: {p1.boat.pos_x}, Y: {p1.boat.pos_y}\nSupplies: {p1.boat.supply}"), True, (128, 128, 128))




        # Display Flip
        #print(f"boat is at: {x} {y}")
        pygame.display.update()
        


        # Clock 
        dt = clock.tick(constants.FRAMERATE) / 1000
        #print("Delta: " + dt)


if __name__ == "__main__":
    main()
