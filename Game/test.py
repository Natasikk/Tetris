import pygame as pg


class Main:
    def __int__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.run = True

    def main_loop(self):
        while self.run:
            pg.display.update()


main = Main()
main.main_loop()
pg.quit()
