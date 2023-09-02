import sys
import pygame

from settings import Settings

class Tetris:
    """Класс для управления игрой."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Tetris')
    

    def run_game(self):
        """Запуск основного цикла игры."""
        if self.settings.game_active:
            pass

        self._update_screen()
    

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        
        pygame.display.flip()

