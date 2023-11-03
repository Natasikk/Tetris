from Settings import *


class Figures:
    def __init__(self):
        self.content = []

    def append(self, fig):
        self.content.append(fig)

    def move_down(self):
        for i in self.content:
            if i.pos[1] + max([i[1] for i in i.cords]) < 19:
                i.pos[1] += 1


class Figure:
    def __init__(self):
        self.color = RED
        self.cords = [(0, 0), (1, 0), (0, 1), (0, 2)]
        self.pos = [4, 0]

    def move(self, direction):
        if direction == 0:
            if self.pos[0] + max([i[0] for i in self.cords]) < 9:
                self.pos[0] += 1
        elif direction == 1:
            if self.pos[1] + max([i[1] for i in self.cords]) < 19:
                self.pos[1] += 1
        elif direction == 2:
            if self.pos[0] > 0:
                self.pos[0] -= 1
