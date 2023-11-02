import pygame
from Settings import *
from Figure import Figure


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.figures = []
        self.tick = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def main_loop(self):
        while self.run:
            self.tick += 1
            print(self.tick)
            self.clock.tick(FPS)
            pygame.display.set_caption(str(self.clock.get_fps()))
            if self.tick % 300 == 0:
                self.figures.append(Figure())
            self.events()
            self.render()
            pygame.display.update()

    def render(self):
        for j in range(H):
            for i in range(W):
                pygame.draw.rect(self.screen, WHITE, (i*TILE, j*TILE, TILE, TILE), 1)

        for item in self.figures:
            for cords in item.cords:
                pygame.draw.rect(self.screen, item.color, ((4 + cords[0]) * TILE, cords[1] * TILE, TILE, TILE))


main = Main()
main.main_loop()
