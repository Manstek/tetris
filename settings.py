class Settings:
    """Класс для управления настройками игры."""
    def __init__(self):
        self.screen_width = 200
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        self.game_active = True

        self.base_figure_width = 20
        self.base_figure_height = 20
        self.figure_color = (0, 0, 0)

        self.field_width = 100
        self.field_height = 300
        self.step = 20

        
