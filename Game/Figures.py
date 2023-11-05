from Settings import *


class Figures:
    def __init__(self):
        self.passive = []
        self.active = Figure()

    def append(self, fig):
        self.passive.append(fig)

    def add_to_passive(self):
        self.passive.append(self.active)
        for cord in self.active.cords:
            a_ = (cord[0] + self.active.pos[0], cord[1] + self.active.pos[1] - 1)
        self.active = Figure()


class Figure:
    def __init__(self):
        self.color = RED
        self.cords = [(0, 0), (1, 0), (0, 1), (0, 2)]
        self.pos = [4, 0]

    def move(self, figures, direction):
        flag = True
        if direction == 0:
            for cord in self.cords:
                if self.pos[0] + cord[0] > 8:
                    flag = False
                for fig_ in figures:
                    for cord_ in fig_.cords:
                        if (self.pos[0] + cord[0] + 1, self.pos[1] + cord[1]) == (fig_.pos[0] + cord_[0],
                                                                                  fig_.pos[1] + cord_[1]):
                            flag = False
            if flag:
                self.pos[0] += 1

        elif direction == 1:
            for cord in self.cords:
                if self.pos[1] + cord[1] > 18:
                    flag = False
                for fig_ in figures:
                    for cord_ in fig_.cords:
                        if (self.pos[0] + cord[0], self.pos[1] + cord[1] + 1) == (fig_.pos[0] + cord_[0],
                                                                                  fig_.pos[1] + cord_[1]):
                            flag = False
            if flag:
                self.pos[1] += 1
            else:
                return False
        elif direction == 2:
            if self.pos[0] < 1:
                flag = False
            for cord in self.cords:
                for fig_ in figures:
                    for cord_ in fig_.cords:
                        if (self.pos[0] + cord[0] - 1, self.pos[1] + cord[1]) == (fig_.pos[0] + cord_[0],
                                                                                  fig_.pos[1] + cord_[1]):
                            flag = False
            if flag:
                self.pos[0] -= 1
        return True
