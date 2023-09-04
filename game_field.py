import pygame
from settings import Settings 
from pygame.sprite import Sprite


class GameField(Sprite):
    """Класс, отвечающий за игровое поле."""
    def __init__(self, tetris):
        super().__init__()
        self.settings = Settings()
        self.screen = tetris.screen
        self.line = pygame.draw.line(self.screen, self.settings.figure_color, (0, 0), (100, 300))
        


    def create_game_field(self):
        """Функция для создания обратного 'стакана' игрового поля."""
        # field - weidht = 100, height = 300 pygame.polygon
        for x in range(50, self.settings.field_width + self.settings.step + 50, self.settings.step):
            for y in range(100, self.settings.field_height + self.settings.step + 100, self.settings.step):      
                pygame.draw.line(self.screen, self.settings.figure_color, (x, y), (x, self.settings.field_height))
                pygame.draw.line(self.screen, self.settings.figure_color, (x, y), (self.settings.field_width, y))
