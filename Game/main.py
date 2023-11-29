import pygame
from Settings import *
from Figures import Figures


def in_box(pos, box):
    if (pos[0] >= box[0]) and pos[0] <= box[0] + box[2]:
        if (pos[1] >= box[1]) and pos[1] <= box[1] + box[3]:
            return True
    return False


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.figures = Figures()
        self.tick = 0
        self.speed = 1
        self.best_score = 0
        self.pause_btn = (450, 550, 50, 50)
        self.return_btn = (225, 300, 125, 50)
        self.exit_to_menu_btn = (225, 375, 125, 50)
        self.pause = False
        self.menu = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if self.menu:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if in_box(pygame.mouse.get_pos(), self.return_btn):
                            self.menu = False
                            self.tick = 0
                            self.figures = Figures()
                            file = open('best_score.txt', 'r')
                            self.best_score = int(file.read())
            elif self.pause:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if in_box(pygame.mouse.get_pos(), self.return_btn):
                            self.pause = False
                        elif in_box(pygame.mouse.get_pos(), self.exit_to_menu_btn):
                            self.pause = False
                            self.menu = True
                            self.save_score()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.pause = False
            else:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.figures.active.rotate(self.figures.colors)
                    elif event.key == pygame.K_ESCAPE:
                        self.pause = True
                    else:
                        d_ = 0
                        if event.key == pygame.K_RIGHT:
                            d_ = 0
                        elif event.key == pygame.K_DOWN:
                            d_ = 1
                        elif event.key == pygame.K_LEFT:
                            d_ = 2
                        if not self.figures.active.move(self.figures.colors, d_):
                            self.figures.add_to_passive()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if in_box(pygame.mouse.get_pos(), self.pause_btn):
                            self.pause = True

    def save_score(self):
        if self.figures.score > self.best_score:
            print('f')
            file = open('best_score.txt', 'w')
            file.write(str(self.figures.score))

    def main_loop(self):
        while self.run:
            self.clock.tick(FPS)
            self.events()
            if self.menu:
                self.screen.fill(GREY)
                pygame.draw.rect(self.screen, WHITE, (175, 175, 225, 325), 3)
                pygame.draw.rect(self.screen, GREEN, self.return_btn)
                f1 = pygame.font.Font(None, 60)
                text = f1.render(str('MENU'), True, WHITE)
                self.screen.blit(text, (218, 220))
            elif self.pause:
                pygame.draw.rect(self.screen, GREY, (175, 175, 225, 325))
                pygame.draw.rect(self.screen, WHITE, (175, 175, 225, 325), 3)
                pygame.draw.rect(self.screen, GREEN, self.return_btn)
                pygame.draw.rect(self.screen, RED, self.exit_to_menu_btn)
                f1 = pygame.font.Font(None, 60)
                text = f1.render(str('PAUSE'), True, WHITE)
                self.screen.blit(text, (218, 220))
            else:
                if self.figures.score < 100:
                    self.speed = 1
                elif self.figures.score < 200:
                    self.speed = 1.5
                elif self.figures.score < 300:
                    self.speed = 2
                elif self.figures.score < 400:
                    self.speed = 2.5
                elif self.figures.score < 500:
                    self.speed = 3
                elif self.figures.score < 600:
                    self.speed = 3.5
                elif self.figures.score < 700:
                    self.speed = 4
                elif self.figures.score < 800:
                    self.speed = 4.5
                elif self.figures.score < 900:
                    self.speed = 5
                elif self.figures.score < 1000:
                    self.speed = 5.5
                self.tick += 1
                if self.tick % (FPS // self.speed) == 0:
                    if not self.figures.active.move(self.figures.colors, 1):
                        self.figures.add_to_passive()
                        for cord in self.figures.active.cords:
                            if self.figures.colors[(cord[0] + self.figures.active.pos[0],
                                                    cord[1] + self.figures.active.pos[1])] is not None:
                                self.menu = True
                                self.save_score()
                pygame.display.set_caption(str(self.clock.get_fps()))
                self.render()
            pygame.display.update()
        pygame.quit()

    def render(self):
        self.screen.fill(GREY)

        pygame.draw.rect(self.screen, WHITE, self.pause_btn, 2)
        pygame.draw.rect(self.screen, WHITE, (460, 555, 8, 40))
        pygame.draw.rect(self.screen, WHITE, (480, 555, 8, 40))

        # next
        pygame.draw.rect(self.screen, BLACK, (370, 400, 200, 120), 2)
        for cord in self.figures.next.cords:
            pygame.draw.rect(self.screen, self.figures.next.color, (400 + cord[0] * TILE, 420 + cord[1] * TILE, TILE, TILE))
            pygame.draw.rect(self.screen, BLACK, (400 + cord[0] * TILE, 420 + cord[1] * TILE, TILE, TILE), 1)

        # active
        for cord in self.figures.active.cords:
            pygame.draw.rect(self.screen, self.figures.active.color, ((self.figures.active.pos[0] + cord[0]) * TILE,
                                                                      (self.figures.active.pos[1] + cord[1]) * TILE,
                                                                      TILE, TILE))
        # passive
        for cord in self.figures.colors:
            if self.figures.colors[cord] is not None:
                pygame.draw.rect(self.screen, self.figures.colors[cord], (cord[0] * TILE, cord[1] * TILE, TILE, TILE))

        # rects
        for j in range(H):
            for i in range(W):
                pygame.draw.rect(self.screen, BLACK, (i * TILE, j * TILE, TILE, TILE), 1)

        # score
        f1 = pygame.font.Font(None, 40)
        text = f1.render(str('SCORE'), True, WHITE)
        text1 = f1.render(str(self.figures.score), True, WHITE)
        self.screen.blit(text, (420, 50))
        self.screen.blit(text1, (460, 100))

        # best_score
        text = f1.render(str('BEST_SCORE'), True, WHITE)
        text1 = f1.render(str(self.best_score), True, WHITE)
        self.screen.blit(text, (380, 150))
        self.screen.blit(text1, (460, 200))


main = Main()
main.main_loop()
