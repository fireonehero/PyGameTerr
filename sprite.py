import pygame
from pygame.sprite import _Group
from globals import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)