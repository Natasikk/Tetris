import pygame
from Settings import *


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def main_loop(self):
        while self.run:
            self.clock.tick(FPS)
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.events()
            self.render()
            pygame.display.update()

    def render(self):
        for j in range(H):
            for i in range(W):
                pygame.draw.rect(self.screen, WHITE, (i*TILE, j*TILE, TILE, TILE), 1)


main = Main()
main.main_loop()
