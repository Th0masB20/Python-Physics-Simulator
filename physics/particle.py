import pygame
from physics.Constants import *
from physics.kinematics import set_velocity

class Particle:
    def __init__(self, x_pos, y_pos, initial_v, color=(255,0,0)):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = SMALL_PARTICLE_SIZE[0]
        self.height = SMALL_PARTICLE_SIZE[1]
        self.velocity = initial_v
        self.color = color
        self.particle = pygame.Rect((x_pos, y_pos, self.width, self.height))
        
    def update_particle(self, window: pygame.Surface):
        pygame.draw.rect(window, self.color, self.particle)
        if(self.x_pos >= 0 and self.x_pos + SMALL_PARTICLE_SIZE[0] - 5 < window.get_width() and self.y_pos >= 0 and self.y_pos + SMALL_PARTICLE_SIZE[1] < window.get_height() - 40):
            self.x_pos, self.y_pos = set_velocity(self.particle, self.x_pos, self.y_pos, self.velocity)
        elif not (self.x_pos > 0 and self.x_pos + SMALL_PARTICLE_SIZE[0] - 5 < window.get_width() ):
            self.velocity = (-1*self.velocity[0], self.velocity[1])
            self.x_pos, self.y_pos = set_velocity(self.particle, self.x_pos, self.y_pos, self.velocity)
        elif not (self.y_pos > 0 and self.y_pos + SMALL_PARTICLE_SIZE[1] < window.get_height() - 40):
            self.velocity = (self.velocity[0], -1*self.velocity[1])
            self.x_pos, self.y_pos = set_velocity(self.particle, self.x_pos, self.y_pos, self.velocity)
    def check_collision(self):                    
        return