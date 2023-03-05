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
                 ):
        if font:
            self.font = pg.font.Font(font, fontSize)
        else:
            self.font = pg.font.SysFont('Arial', fontSize, bold, italic)

        self.norm = self.font.render(text, antialias, color, bgColor)
        self.text = self.norm
        self.rect = self.text.get_rect(center = pos)
        self.wn = window

    def hover(self, effect):
        mousePos = pg.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            self.text = effect()
        else:
            self.text = self.norm
    
    @hover
    def brighten(self, brightness: tuple | str | None = '#A9A9A9'):
        new = self.text.fill(brightness, special_flags = pg.BLEND_RGB_ADD)
        return new

    @hover
    def darken(self, darkness: tuple | str | None = '#A9A9A9'):
        new = self.text.fill(darkness, special_flags = pg.BLEND_RGB_SUB)
        return new

    @hover
    def scale(self):
        new = self.text = pg.transform.scale(self.text, (self.text.get_width() * 1.5, self.text.get_height() * 1.5))
        return new

    def draw(self):
        self.wn.blit(self.text, self.rect)
