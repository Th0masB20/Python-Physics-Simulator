import pygame
def set_velocity(particle:pygame.Rect, x, y, velocity):
    new_x = x + velocity[0]
    new_y = y + velocity[1]
    particle.center = (round(new_x), round(new_y))
    return (new_x, new_y)
    