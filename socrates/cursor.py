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

class cursor():
    def __init__(self,
                 window: pg.Surface,
                 image: str,
                 scale: float | int | None = 1
                 ):
        self.wn = window
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.rect = self.image.get_rect(center = pg.mouse.get_pos())

    def draw(self):
        self.wn.blit(self.image, self.rect)

    def update(self):
        self.rect.center = pg.mouse.get_pos()
