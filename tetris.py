import sys
import pygame

from settings import Settings
from game_field import GameField

class Tetris:
    """Класс для управления игрой."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Tetris')
        
        self.lines = pygame.sprite.Group()
    

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            if self.settings.game_active:
                self._draw_lines()

            self._update_screen()
    

    def _check_events(self):
        """Обрабатывает действия с клавиатуры и мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    

    def _check_keydown_events(self, event):
        """Обрабатывает нажатия на клавиши."""
        if event.key == pygame.K_q:
            sys.exit()


    def _draw_lines(self):
        """Выводит игровое поле из линий на экран."""
        new_line = GameField(self)
        new_line.create_game_field()
        self.lines.add(new_line)


    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)

        for line in self.lines.sprites():
            line.create_game_field()

        pygame.display.flip()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run_game()
