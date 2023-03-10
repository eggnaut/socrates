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

def createCursor(window: pg.Surface,
                 image: str,
                 scale: float | int | None = 1,
                 mouseVisible: bool | None = False
                 ):
    return _cursor(window, image, scale, mouseVisible)

class _cursor():
    def __init__(self,
                 window: pg.Surface,
                 image: str,
                 scale: float | int | None = 1,
                 mouseVisible: bool | None = False
                 ) -> None:
        self.__wn = window
        self.__image = pg.image.load(image).convert_alpha()
        self.__image = pg.transform.scale(self.__image, (self.__image.get_width() * scale, self.__image.get_height() * scale))
        self.__rect = self.__image.get_rect(center = pg.mouse.get_pos())
        pg.mouse.set_visible(mouseVisible)

    def draw(self) -> None:
        self.__wn.blit(self.__image, self.__rect)

    def update(self) -> None:
        self.__rect.center = pg.mouse.get_pos()
