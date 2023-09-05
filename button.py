import pygame.font

class Button:
    """Класс, отвечающий за кнопки в игре."""
    def __init__(self, tetris, msg):
        self.screen = tetris.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 120
        self.height = 50

        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (200, 50)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

