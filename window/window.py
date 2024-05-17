import pygame
from physics.particle import Particle
from window.button import Py_Button

class Window:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
    
    def start_game_loop(self):
        run = True        
        while run:
            self.screen.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            pygame.display.update();
            
        pygame.quit()