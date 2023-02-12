import pygame
import pyganim

PLATFORM_WIDTH = 32  # Ширина прямоугольника
PLATFORM_HEIGHT = 32  # Высота
PLATFORM_COLOR = "#006262"  # Цвет прямоугольника

ANIMATION_BLOCK_TELEPORT = [
    'levels/portal2.png',
    'levels/portal1.png']

ANIMATION_PRINCESS = [
    'levels/princess_l.png',
    'levels/princess_r.png']


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(
            (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pygame.image.load("levels/platform.png")
        self.rect = pygame.Rect(
            x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("levels/dieBlock.png")


class Princess(Platform):

    def __init__(self, x, y):
        super().__init__(x, y)
        anim = []
        for a in ANIMATION_PRINCESS:
            anim.append((a, 600))
        self.boltAnim = pyganim.PygAnimation(anim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(pygame.Color("#7686ff"))
        self.boltAnim.blit(self.image, (0, 0))


class BlockTeleport(BlockDie):

    def __init__(self,x, y, x1, y1):
        super().__init__(x, y)
        self.x1 = x1
        self.y1 = y1
        anim = []
        for a in ANIMATION_BLOCK_TELEPORT:
            anim.append((a, 600))
        self.boltAnim = pyganim.PygAnimation(anim)
        self.boltAnim.play()

    def update(self):
        #self.image.fill(pygame.Color("#7686ff"))
        self.boltAnim.blit(self.image, (0, 0))


