#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from codigo.Background import Background
from codigo.Const import WIN_WIDTH, WIN_HEIGHT
from codigo.Enemy import Enemy
from codigo.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'level1Bg{i}', position=(WIN_WIDTH,0)))
                return list_bg
            case 'tubarao':
                return Player('tubarao', position=(10, WIN_HEIGHT/2))

            case 'polvo':
                return Enemy('polvo', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))

            case 'peixe-luz':
                return Enemy('peixe-luz', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))

            case 'bomba-pequena':
                return Enemy('bomba-pequena', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))

            case 'cobra':
                return Enemy('cobra', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))

