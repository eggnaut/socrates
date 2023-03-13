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

from sys import exit
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame as pg
pg.init()

def createWindow(name: str | int | float | bytes | None = 'socrates GUI App',
                 icon: str | None = None,
                 size: tuple | None = (600, 600),
                 bgColor: tuple | str | None = '#000000',
                 fps: int | None = None
                 ):
    return _window(name, icon, size, bgColor, fps)

class _window():
    def __init__(self,
                 name: str | int | float | bytes | None = 'socrates GUI App',
                 icon: str | None = None,
                 size: tuple | None = (100, 100),
                 bgColor: tuple | str | None = '#000000',
                 fps: int | None = None
                 ) -> None:
        self.__size = size
        self.__bgColor = bgColor
        self.__clock = pg.time.Clock()
        self.__fps = fps
        self.wn = pg.display.set_mode(self.__size)
        self.wn.fill(self.__bgColor)
        self.__name = name
        pg.display.set_caption(self.__name)
        if icon != None:
            self.__icon = icon
            self.__img = pg.image.load(self.__icon).convert_alpha()
            pg.display.set_icon(self.__img)
    
    def setName(self, name: str | int | float | bytes) -> None:
        self.__name = name
        pg.display.set_caption(str(self.__name))
    
    def setIcon(self, icon: str) -> None:
        self.__icon = icon
        self.__img = pg.image.load(self.__icon).convert_alpha()
        pg.display.set_icon(self.__img)

    def setBg(self, bgColor: tuple | str) -> None:
        self.__bgColor = bgColor
        self.wn.fill(self.__bgColor)
    
    def setFps(self, fps: int) -> None:
        self.__fps = fps
    
    def getFps(self) -> int:
        return self.__clock.get_fps()

    def draw(self) -> None:
        self.wn.fill(self.__bgColor)

    def update(self) -> None:
        pg.display.update()
        if self.__fps != None:
            self.__clock.tick(self.__fps)
        else:
            self.__clock.tick()
        
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                exit()
