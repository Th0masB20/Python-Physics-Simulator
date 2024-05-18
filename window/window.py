import pygame
from physics.Physics_world import Physics_world
from physics.particle import Particle
from window.button import Py_Button

class Window:
    def __init__(self, width, height):
        pygame.init()
        self.window = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.frame = 1000
        self.clock.tick(self.frame)
        self.current_selected_object = None
        self.particle_button = Py_Button(width / 4 - 70 , height - 40, 70, 40, 'Particle', (255,255,255))
        self._physics = Physics_world(self.window, 1/self.frame)
        
    def render_buttons(self):
        self.particle_button.render_button(self.window) 
        if(self.particle_button.is_clicked()):
            self.current_selected_object = 'particle'
            
    def start_game_loop(self):
        run = True        
        while run:
            self.window.fill((0,0,0))
               
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                     if self.current_selected_object == 'particle':
                        mouse_pos = pygame.mouse.get_pos()
                        if mouse_pos[1] < self.window.get_width() - 40: 
                            self._physics.create_particle(mouse_pos[0], mouse_pos[1])
                if event.type == pygame.QUIT:
                    run = False
            
            self.render_buttons() 
            self._physics.update_physics_objects()
            pygame.display.update();
            
        pygame.quit()