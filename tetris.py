import sys
import pygame

from settings import Settings
from game_field import GameField
from base_figure import BaseFigure
from game_stats import GameStats
from button import Button

class Tetris:
    """Класс для управления игрой."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Tetris')
        
        self.lines = pygame.sprite.Group()

        self.square = BaseFigure(self)

        self.stats = GameStats(self)
        self.play_button = Button(self, 'Play')
        self.stop_button = Button(self, 'Stop')
    

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._draw_lines()
            if self.stats.game_active:
                self._update_figure()

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
        elif event.key == pygame.K_RIGHT:
            self.square.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.square.moving_left = True


    def _draw_lines(self):
        """Выводит игровое поле из линий на экран."""
        new_line = GameField(self)
        new_line.create_game_field()
        self.lines.add(new_line)


    def _update_figure(self):
        """Перемещает базовую фигуру."""
        end_line_pos_y = self.settings.screen_height - 2 * self.settings.step
        start_first_line_x = (self.settings.screen_width - self.settings.field_width) // 2
        end_last_line_x = start_first_line_x + 4 * self.settings.step
        if self.square.rect.y < end_line_pos_y and start_first_line_x <= self.square.rect.x <= end_last_line_x:
            self.square.update()


    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)

        for line in self.lines.sprites():
            line.create_game_field()
        
        self.square.create_BaseFigure()

        if not self.stats.game_active:
            self.play_button.draw_button()
        else:
            self.stop_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run_game()
