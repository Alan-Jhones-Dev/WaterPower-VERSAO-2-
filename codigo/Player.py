#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from codigo.Const import ENTITY_SPEED, WIN_HEIGHT
from codigo.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top>0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed[pygame.K_LEFT] and self.rect.left>0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed[pygame.K_RIGHT] and self.rect.right < WIN_HEIGHT:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def run(self):
        pass