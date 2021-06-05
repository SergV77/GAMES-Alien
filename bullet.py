import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблем."""

    def __init__ (self, ai_settings, screen, ship):
        """Создаем объект пули в текущей позиции."""
        super(Bullet, self).__init__()
        self.screen = screen

        #Создаем пули в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Позиция пули храниться в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """премещает пулю вверх по экрану."""
        #Обновление позиции пули в вещественном формате
        self.y -= self.speed_factor
        #обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)