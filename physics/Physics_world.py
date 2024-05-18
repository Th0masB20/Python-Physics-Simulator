from physics.particle import *
import random
import numpy as np

class Physics_world():
    
    def __init__(self, window, delta_time):
        self.window = window
        self.particle_array = []
        self.delta_time = delta_time
        

    def create_particle(self, x, y):
        v_x = random.randint(-100,100)
        v_y = random.randint(-100,100)
        velocity = (v_x * self.delta_time, v_y * self.delta_time)
        new_particle = Particle(x , y, velocity,(random.randint(100,255),random.randint(100,255),random.randint(100,255)))
        self.particle_array.append(new_particle)
        
    def update_physics_objects(self):
        for particles in self.particle_array:
            particles.update_particle(self.window)
            