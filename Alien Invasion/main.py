import sys
import pygame

def run_game():
    #Initialise the game
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #Set background color
    bg_color = (230,0,230)

    #Start main loop of game
    while True:

        #Keyboard mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw the screen during each passing of the loop
        screen.fill(bg_color)

        #show the most recent drawn screen
        pygame.display.flip()

#start the game
run_game()

        
    
