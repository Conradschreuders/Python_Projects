import pygame

#Class to store all settings and movements for the ship
class Ship():
    
    def __init__(self, screen):
        '''Initialise the ship and its starting position'''
        self.screen = screen

        #Load ship image and show on screen and get its rect
        #self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('images/owl.png')
        self.image  = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start the ship each time at the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement of the ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' Update the sips position based on movement flag.'''
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
    
        

    
 
