import pygame
from settings import Settings

class BaseFigure:
    """Базовый квадрат из которого состоят все фигуры."""
    def __init__(self, tetris):
        self.screen = tetris.screen
        self.settings = Settings()
        
        self.start_first_line_x = (self.settings.screen_width - self.settings.field_width) // 2
        self.start_pos_x = self.start_first_line_x + 2 * self.settings.step
        self.start_first_line_y = self.settings.screen_height - self.settings.field_height - self.settings.step
        self.start_pos_y = self.start_first_line_y

        self.rect = pygame.Rect(self.start_pos_x, self.start_pos_y, 
            self.settings.base_figure_width, self.settings.base_figure_height)
    


    def create_BaseFigure(self):
        """Создаёт один базовый квадрат."""
        self.rect = pygame.draw.rect(self.screen, self.settings.base_figure_color, self.rect)



