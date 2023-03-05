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

        self.text = self.font.render(text, antialias, color, bgColor)
        self.rect = self.text.get_rect(center = pos)
        self.wn = window

    def hover(self, effect):
        mousePos = pg.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            return effect
        else:
            pass
    
    @hover
    def brighten(self):
        self.text.fill((169, 169, 169), special_flags = pg.BLEND_RGB_ADD)

    @hover
    def darken(self):
        self.text.fill((169, 169, 169), special_flags = pg.BLEND_RGB_SUB)

    @hover
    def scale(self):
        self.text = pg.transform.scale(self.text, (self.text.get_width() * 1.5, self.text.get_height() * 1.5))

    def draw(self):
        self.wn.blit(self.text, self.rect)
