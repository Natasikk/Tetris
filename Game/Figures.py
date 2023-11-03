from Settings import *


class Figures:
    def __init__(self):
        self.passive = []
        self.active = Figure()
        self.floor = {i: [19] for i in range(10)}

    def append(self, fig):
        self.passive.append(fig)

    def move_down(self):
        if self.check():
            self.active.pos[1] += 1

    def add_to_passive(self):
        self.passive.append(self.active)
        for cord in self.active.cords:
            a_ = (cord[0] + self.active.pos[0], cord[1] + self.active.pos[1] - 1)
            self.floor[a_[0]].append(a_[1])
        self.active = Figure()


    def check(self):
        for cord in self.active.cords:
            x, y = cord[0], cord[1]
            x += self.active.pos[0]
            y += self.active.pos[1]
            for y_ in self.floor[x]:
                if y == y_:
                    return False
        return True


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
            self.pos[1] += 1
        elif direction == 2:
            if self.pos[0] > 0:
                self.pos[0] -= 1
