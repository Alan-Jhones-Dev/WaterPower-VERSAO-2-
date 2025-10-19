#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from codigo.Const import COLOR_BLUE, COLOR_SEA_BLUE, WIN_WIDTH, MENU_OPTION, COLOR_SEA_GREEN, COLOR_WHITE


class Menu:
        def __init__(self, window):
            self.window = window
            self.surf = pygame.image.load('asset/menuBg.png').convert_alpha()
            self.rect = self.surf.get_rect(left=0, top=0)

        def run(self):
            menu_option = 0
            #pygame.mixer.music.load('asset/musicaMenu.wav')
            #pygame.mixer.music.play(-1)
            while True:

                self.window.blit(source=self.surf, dest=self.rect)
                self.menu_text(50, 'Water', COLOR_BLUE, ((WIN_WIDTH / 2), 70))
                self.menu_text(50, 'Power', COLOR_SEA_BLUE, ((WIN_WIDTH / 2), 120))

                for i in range(len(MENU_OPTION)):
                    if i == menu_option:
                        self.menu_text(25, MENU_OPTION[i], COLOR_SEA_GREEN, ((WIN_WIDTH / 2), 200 + 40 * i))
                    else:
                        self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 40 * i))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()  # Close Window
                        quit()
                    if event.type == pygame.KEYDOWN:  # KEY EVENTS
                        if event.key == pygame.K_DOWN:  # DOWN KEY
                            if menu_option < len(MENU_OPTION) - 1:
                                menu_option += 1
                            else:
                                menu_option = 0
                        if event.key == pygame.K_UP:  # UP KEY
                            if menu_option > 0:
                                menu_option -= 1
                            else:
                                menu_option = len(MENU_OPTION) - 1

                        if event.key == pygame.K_RETURN:  # ENTER
                            return MENU_OPTION[menu_option]

        def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="African", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)
