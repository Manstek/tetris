class Settings:
    """Класс для управления настройками игры."""
    def __init__(self):
        self.screen_width = 400
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.game_active = True

        self.base_figure_width = 40
        self.base_figure_height = 40
        self.base_figure_color = (255, 255, 255)
        self.base_figure_speed_y = 2.5
        self.base_figure_speed_x = 40

        self.field_color = (0, 255, 0)
        self.field_width = 200
        self.field_height = 600
        self.step = 40

        
