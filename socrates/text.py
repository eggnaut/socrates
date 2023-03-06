#    Under construction!
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

import pygame as pg
pg.init()

class text():
    def __init__(self, 
                 window: pg.Surface,
                 text: str | bytes,
                 font: str | None = 'Arial',
                 fontSize: int | None = 20,
                 bold: bool | None = False, 
                 italic: bool | None = False,
                 antialias: bool | None = True,
                 color: tuple | str | None = '#000000',
                 bgColor: tuple | str | None = '#FFFFFF',
                 pos: tuple | None = (0, 0)
                 ) -> None:
        if font:
            self.font = pg.font.Font(font, fontSize)
        else:
            self.font = pg.font.SysFont('Arial', fontSize, bold, italic)

        self.pos = pos
        self.norm = self.font.render(text, antialias, color, bgColor)
        self.text = self.norm
        self.rect = self.text.get_rect(center = self.pos)
        self.wn = window

    def hover(self, scale: float | int | None = 1.25) -> None:
        mousePos = pg.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            new = pg.transform.scale(self.norm, (self.norm.get_width() * scale, self.norm.get_height() * scale))
            self.text = new
            self.rect = self.text.get_rect(center = self.pos)
        else:
            self.text = self.norm
            self.rect = self.text.get_rect(center = self.pos)

    def draw(self) -> None:
        self.wn.blit(self.text, self.rect)
    
    def update(self) -> None:
        pass
