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