import pygame

from .constants import RED, WIDTH, HEIGHT


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 0 + self.rect.height)

    def update(self):
        self.rect.y += 5

        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
