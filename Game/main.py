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
                if event.key == pygame.K_RIGHT:
                    self.figures.active.move(0)
                elif event.key == pygame.K_DOWN:
                    self.figures.active.move(1)
                elif event.key == pygame.K_LEFT:
                    self.figures.active.move(2)


    def main_loop(self):
        while self.run:
            self.tick += 1
            if self.tick % 30 == 0:
                self.figures.move_down()
            if not self.figures.check():
                self.figures.add_to_passive()
            self.clock.tick(FPS)
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.events()
            self.render()
            pygame.display.update()


    def render(self):
        self.screen.fill(BLACK)

        # floor
        for x_ in range(10):
            for y_ in self.figures.floor[x_]:
                pygame.draw.rect(self.screen, GREEN, (x_ * TILE, y_ * TILE, TILE, TILE))

        # rects
        for j in range(H):
            for i in range(W):
                pygame.draw.rect(self.screen, WHITE, (i*TILE, j*TILE, TILE, TILE), 1)

        # figures
        for item in self.figures.passive + [self.figures.active]:
            try:
                for cords in item.cords:
                    pygame.draw.rect(self.screen, item.color, ((item.pos[0] + cords[0]) * TILE,
                                                               (item.pos[1] + cords[1]) * TILE, TILE, TILE))
            except:
                pass



main = Main()
main.main_loop()
