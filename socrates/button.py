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
                 pos: tuple | None = (0, 0)
                 ):
    return button(window, image, scale, pos)

class button():
    def __init__(self,
                 window: pg.Surface,
                 image: str,
                 scale: float | int | None = 1,
                 pos: tuple | None = (0, 0)
                 ):
        self.wn = window
        self.pos = pos
        self.norm = pg.image.load(image).convert_alpha()
        self.norm = pg.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.image = self.norm
        self.rect = self.image.get_rect(center = self.pos)
    
    def hover(self, scale: float | int | None = 1.25) -> None:
        mousePos = pg.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            new = pg.transform.scale(self.norm, (self.norm.get_width() * scale, self.norm.get_height() * scale))
            self.image = new
            self.rect = self.image.get_rect(center = self.pos)
        else:
            self.image = self.norm
            self.rect = self.image.get_rect(center = self.pos)

    def action(self):
        pass

    def draw(self) -> None:
        self.wn.blit(self.image, self.rect)
    
    def update(self) -> None:
        mousePos = pg.mouse.get_pos()

        for ev in pg.event.get():
            if pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(mousePos):
                    self.action()
