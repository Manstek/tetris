import pygame
from settings import Settings 
from pygame.sprite import Sprite


class GameField(Sprite):
    """Класс, отвечающий за игровое поле."""
    def __init__(self, tetris):
        super().__init__()
        self.settings = Settings()
        self.screen = tetris.screen
        self.line = pygame.draw.line(self.screen, self.settings.field_color, (0, 0), (100, 300))

        self.start_pos_x = (self.settings.screen_width - self.settings.field_width) // 2
        self.start_pos_y = self.settings.screen_height - self.settings.field_height - self.settings.step
        self.end_pos_x = self.settings.field_width + self.settings.step + self.start_pos_x
        self.end_pos_y = self.settings.field_height + self.settings.step + self.start_pos_y


    def create_game_field(self):
        """Функция для создания обратного 'стакана' игрового поля."""
        # field - weidht = 100, height = 300
        for x in range(self.start_pos_x, self.end_pos_x, self.settings.step):
            for y in range(self.start_pos_y, self.end_pos_y, self.settings.step):      
                pygame.draw.line(self.screen, self.settings.field_color, (x, y), (x, self.settings.field_height))
                pygame.draw.line(self.screen, self.settings.field_color, (x, y), (self.settings.field_width, y))
