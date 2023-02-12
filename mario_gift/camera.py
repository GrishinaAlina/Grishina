import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


class Camera:

    def __init__(self, width, height):
        self.func = self.camera_conf
        self.state = pygame.Rect(0, 0, width, height)

    def update(self, hero):
        self.state = self.func(self.state, hero.rect)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    @staticmethod
    def camera_conf(camera, hero):
        _, _, w, h = camera
        x, y, _, _ = hero

        x = -x + WIN_WIDTH / 2
        y = -y + WIN_HEIGHT / 2

        x = min(0, x)
        y = min(0, y)

        x = max(camera.width - WIN_WIDTH/2.5, x)
        y = max(camera.height - WIN_HEIGHT/2.1, y)

        return pygame.Rect(x, y, w, h)
