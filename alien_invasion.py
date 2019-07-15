import pygame
import game_functions as gf
from ship import Ship
from settings import Settings

def run_game():
    #Initialise the game, settings and screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    #Make a ship
    ship = Ship(screen)
    
    #Start main loop of game
    while True:
        #Check for events
        gf.check_events()   

        #Redraw the screen during each passing of the loop
        gf.update_screen(ai_settings, screen, ship)
        
        
    
#start the game
run_game()

        
    
