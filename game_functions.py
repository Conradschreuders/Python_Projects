import sys
import pygame


def check_events(ship):
    """Respond to key presses and mouse events."""
    #Keyboard mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move the ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                #Move the ship to the left
                ship.moving_left = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #Stop moving to the right
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                #Stop moving to the left
                ship.moving_left = False
                
                


def update_screen(ai_settings, screen, ship):
    """ Update the screen and images """
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Make mist recent drawn image visible
    pygame.display.flip()
        
