#    A GUI framework for Python built on-top of the Pygame library.
#    Copyright (C) 2023  Dishant B. (eggnaut)
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame as pg
pg.init()

def createButton(window: pg.Surface,
                 image: str,
                 scale: float | int | None = 1,
                 pos: tuple | None = (0, 0),
                 action = None
                 ):
    return _button(window, image, scale, pos, action)

class _button():
    def __init__(self,
                 window: pg.Surface,
                 image: str,
                 scale: float | int | None = 1,
                 pos: tuple | None = (0, 0),
                 action = None
                 ):
        self.__wn = window
        self.__pos = pos
        self.__action = action
        self.__doAction = self.__action
        self.__click = False
        self.__norm = pg.image.load(image).convert_alpha()
        self.__norm = pg.transform.scale(self.__norm, (self.__norm.get_width() * scale, self.__norm.get_height() * scale))
        self.__image = self.__norm
        self.__rect = self.__image.get_rect(center = self.__pos)
    
    def hover(self, scale: float | int | None = 1.25) -> None:
        __mousePos = pg.mouse.get_pos()

        if self.__rect.collidepoint(__mousePos):
            new = pg.transform.scale(self.__norm, (self.__norm.get_width() * scale, self.__norm.get_height() * scale))
            self.__image = new
            self.__rect = self.__image.get_rect(center = self.__pos)
        else:
            self.__image = self.__norm
            self.__rect = self.__image.get_rect(center = self.__pos)

    def __doAction(self):
        pass

    def draw(self) -> None:
        self.__wn.blit(self.__image, self.__rect)
    
    def update(self):
        __mousePos = pg.mouse.get_pos()

        if pg.mouse.get_pressed()[0] and self.__rect.collidepoint(__mousePos) and not self.__click:
            self.__doAction()
            self.__click = pg.mouse.get_pressed()[0]
