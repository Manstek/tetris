import pygame
from settings import Settings


class BaseFigure:
    """Базовый квадрат из которого состоят все фигуры."""
    def __init__(self, tetris):
        self.screen = tetris.screen
        self.settings = Settings()

        self.moving_right = False
        self.moving_left = False
        
        self.start_first_line_x = (self.settings.screen_width - self.settings.field_width) // 2
        self.start_pos_x = self.start_first_line_x + 2 * self.settings.step
        self.start_first_line_y = self.settings.screen_height - self.settings.field_height - self.settings.step
        self.start_pos_y = self.start_first_line_y

        self.rect = pygame.Rect(self.start_pos_x, self.start_pos_y, 
            self.settings.base_figure_width, self.settings.base_figure_height)
    
        self.x= float(self.rect.x)
        self.y = float(self.rect.y)

    def create_BaseFigure(self):
        """Создаёт один базовый квадрат."""
        self.rect = pygame.draw.rect(self.screen, self.settings.base_figure_color, self.rect)

    
    def update(self):
        """Перемещает фигуру на один квадрат вниз (40х40)."""
        self.y += self.settings.base_figure_speed_y
        self.rect.y = self.y

        if self.moving_right:
            if self.rect.x < self.start_first_line_x + 4 * self.settings.step:
                self.x += self.settings.base_figure_speed_x
                self.rect.x = self.x
                self.moving_right = False
        if self.moving_left:
            if self.rect.x > self.start_first_line_x:
                self.x -= self.settings.base_figure_speed_x
                self.rect.x = self.x
                self.moving_left = False

