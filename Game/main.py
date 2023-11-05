import pygame
from Settings import *
from Figures import Figures, Figure


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.figures = Figures()
        self.tick = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.figures.active.rotate(self.figures.passive)
                else:
                    d_ = 0
                    if event.key == pygame.K_RIGHT:
                        d_ = 0
                    elif event.key == pygame.K_DOWN:
                        d_ = 1
                    elif event.key == pygame.K_LEFT:
                        d_ = 2
                    if not self.figures.active.move(self.figures.passive, d_):
                        self.figures.add_to_passive()


    def main_loop(self):
        while self.run:
            self.clock.tick(FPS)
            self.tick += 1
            if self.tick % FPS == 0:
                if not self.figures.active.move(self.figures.passive, 1):
                    self.figures.add_to_passive()
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.events()
            self.render()
            pygame.display.update()


    def render(self):
        self.screen.fill(BLACK)

        # figures
        for cord in self.figures.active.cords:
            pygame.draw.rect(self.screen, self.figures.active.color, ((self.figures.active.pos[0] + cord[0]) * TILE,
                                                (self.figures.active.pos[1] + cord[1]) * TILE, TILE, TILE))
        for cord in self.figures.passive:
            pygame.draw.rect(self.screen, self.figures.passive[cord], (cord[0] * TILE, cord[1] * TILE, TILE, TILE))


        # rects
        for j in range(H):
            for i in range(W):
                pygame.draw.rect(self.screen, WHITE, (i*TILE, j*TILE, TILE, TILE), 1)





main = Main()
main.main_loop()
