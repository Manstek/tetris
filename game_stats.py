class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, tetris):
        self.settings = tetris.settings
        self.reset_stats()

        self.game_active = True
    

    def reset_stats(self):
        """"Инициализирует статистику, изменяющуюся в ходе игры."""
        pass