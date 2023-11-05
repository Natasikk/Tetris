from Settings import *


class Figures:
    def __init__(self):
        self.passive = []
        self.active = Figure()

    def add_to_passive(self):
        for cord in self.active.cords:
            a_ = [cord[0] + self.active.pos[0], cord[1] + self.active.pos[1]]
            self.passive.append(a_)
        self.active = Figure()
        self.delete_line()

    def delete_line(self):
        for y_ in range(H):
            count = []
            for cord in self.passive:
                if cord[1] == y_:
                    count.append(cord)
            if len(count) == W:
                for cord_ in count:
                    self.passive.remove(cord_)
                for cord in self.passive:
                    cord[1] += 1


class Figure:
    def __init__(self):
        self.color = RED
        self.cords = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        self.pos = [4, 0]

    def move(self, figures, direction):
        flag = True
        if direction == 0:
            for cord in self.cords:
                if self.pos[0] + cord[0] > 8:
                    flag = False
                for cord_ in figures:
                    if [self.pos[0] + cord[0] + 1, self.pos[1] + cord[1]] == cord_:
                        flag = False
            if flag:
                self.pos[0] += 1

        elif direction == 1:
            for cord in self.cords:
                if self.pos[1] + cord[1] > 18:
                    flag = False
                for cord_ in figures:
                    if [self.pos[0] + cord[0], self.pos[1] + cord[1] + 1] == cord_:
                        flag = False
            if flag:
                self.pos[1] += 1
            else:
                return False
        elif direction == 2:
            if self.pos[0] < 1:
                flag = False
            for cord in self.cords:
                for cord_ in figures:
                    if [self.pos[0] + cord[0] - 1, self.pos[1] + cord[1]] == cord_:
                        flag = False
            if flag:
                self.pos[0] -= 1
        return True
