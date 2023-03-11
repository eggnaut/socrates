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

import socrates as sc

window = sc.window.createWindow(size = (600, 600))
cursor = sc.cursor.createCursor(window.wn, './docs/logo.png', 0.0625)
text = sc.text.text(window.wn, 'socrates', pos = (300, 300))

while True:
    window.update()
    window.draw()

    cursor.update()
    cursor.draw()

    text.update()
    text.draw()