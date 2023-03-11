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
                 size: tuple | None = (100, 100),
                 bgColor: tuple | str | None = '#000000',
                 fps: int | None = None
                 ):
    return window(name, icon, size, bgColor, fps)

class window():
    def __init__(self,
                 name: str | int | float | bytes | None = 'socrates GUI App',
                 icon: str | None = None,
                 size: tuple | None = (100, 100),
                 bgColor: tuple | str | None = '#000000',
                 fps: int | None = None
                 ) -> None:
        self.size = size
        self.bgColor = bgColor
        self.clock = pg.time.Clock()
        self.fps = fps
        self.wn = pg.display.set_mode(self.size)
        self.wn.fill(self.bgColor)
        self.name = name
        pg.display.set_caption(self.name)
        if icon != None:
            self.icon = icon
            self.img = pg.image.load(self.icon).convert_alpha()
            pg.display.set_icon(self.img)
    
    def setName(self, name: str | int | float | bytes) -> None:
        self.name = name
        pg.display.set_caption(str(self.name))
    
    def setIcon(self, icon: str) -> None:
        self.icon = icon
        self.img = pg.image.load(self.icon).convert_alpha()
        pg.display.set_icon(self.img)

    def setBg(self, bgColor: tuple | str) -> None:
        self.bgColor = bgColor
        self.wn.fill(self.bgColor)
    
    def setFps(self, fps: int) -> None:
        self.fps = fps
    
    def getFps(self) -> int:
        return self.clock.get_fps()

    def draw(self) -> None:
        self.wn.fill(self.bgColor)

    def update(self) -> None:
        pg.display.update()
        if self.fps != None:
            self.clock.tick(self.fps)
        else:
            self.clock.tick()
        
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                exit()
