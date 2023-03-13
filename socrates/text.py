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

def createText(window: pg.Surface,
                 content: str | bytes | int | float,
                 font: str | None = None,
                 fontSize: int | None = 20,
                 bold: bool | None = False, 
                 italic: bool | None = False,
                 antialias: bool | None = True,
                 color: tuple | str | None = '#000000',
                 bgColor: tuple | str | None = '#FFFFFF',
                 pos: tuple | None = (0, 0)
                 ):
    return _text(window, content, font, fontSize, bold, italic, antialias, color, bgColor, pos)

class _text():
    def __init__(self, 
                 window: pg.Surface,
                 content: str | bytes | int | float,
                 font: str | None = None,
                 fontSize: int | None = 20,
                 bold: bool | None = False, 
                 italic: bool | None = False,
                 antialias: bool | None = True,
                 color: tuple | str | None = '#000000',
                 bgColor: tuple | str | None = '#FFFFFF',
                 pos: tuple | None = (0, 0)
                 ) -> None:
        if font != None:
            self.__font = pg.font.Font(font, fontSize)
        else:
            self.__font = pg.font.SysFont('Arial', fontSize, bold, italic)

        self.__pos = pos
        self.__norm = self.__font.render(content, antialias, color, bgColor)
        self.__content = self.__norm
        self.__rect = self.__content.get_rect(center = self.__pos)
        self.__wn = window

    def hover(self, scale: float | int | None = 1.25) -> None:
        mousePos = pg.mouse.get_pos()

        if self.__rect.collidepoint(mousePos):
            new = pg.transform.scale(self.__norm, (self.__norm.get_width() * scale, self.__norm.get_height() * scale))
            self.__content = new
            self.__rect = self.__content.get_rect(center = self.__pos)
        else:
            self.__content = self.__norm
            self.__rect = self.__content.get_rect(center = self.__pos)

    def draw(self) -> None:
        self.__wn.blit(self.__content, self.__rect)
    
    def update(self) -> None:
        pass
