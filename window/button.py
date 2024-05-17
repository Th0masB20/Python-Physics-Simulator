import pygame

class Py_Button:
    def __init__(self,x_pos, y_pos, width, height, text, color):
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.Button = pygame.Rect((x_pos, y_pos, width, height))
        self.text = text
        self.text_font = pygame.font.SysFont('georgia', 15)
    
    def render_button(self, screen: pygame.Surface):
        render_text = self.text_font.render(self.text, True, 'black')
        pygame.draw.rect(screen, self.color, self.Button)
        screen.blit(render_text, (self.x_pos + (self.width - render_text.get_width())/2, self.y_pos + (self.height - render_text.get_height())/2))
        
    def is_clicked(self):
        in_button = ( self.x_pos < pygame.mouse.get_pos()[0] < self.x_pos + self.width) and ( self.y_pos < pygame.mouse.get_pos()[1] < self.y_pos + self.height)
        return in_button
            
    
    
        