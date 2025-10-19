#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.transform

from codigo.Const import WIN_WIDTH, ENTITY_SPEED
from codigo.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass

    def run(self):
        pass