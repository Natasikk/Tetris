from Settings import *
import random


class Figures:
    def __init__(self):
        self.colors = {(x, y): None for x in range(W) for y in range(H)}
        self.active = Figure()
        self.next = Figure()
        self.score = 0

    def add_to_passive(self):
        for cord in self.active.cords:
            a_ = (cord[0] + self.active.pos[0], cord[1] + self.active.pos[1])
            self.colors[a_] = self.active.color
        self.active = self.next
        self.next = Figure()
        self.delete_line()

    def delete_line(self):
        c_ = 1
        for y_ in range(H):
            count = []
            for cord in self.colors:
                if cord[1] == y_ and self.colors[cord] is not None:
                    count.append(cord)
            if len(count) == W:
                for cord_ in count:
                    self.colors[cord_] = None
                del_ = {}
                for cord in self.colors:
                    if cord[1] < y_:
                        del_[(cord[0], cord[1] + 1)] = self.colors[cord]
                        self.colors[cord] = None
                for cord in del_:
                    self.colors[cord] = del_[cord]
                self.score += c_ * 10
                c_ += 1


class Figure:
    def __init__(self):
        self.colors = [BLUE, ORANGE, TURQUOISE, YELLOW, GREEN, RED, VIOLET]
        i_ = random.randint(0, 6)
        self.cords_rotates = [[[(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (0, 1), (0, 2)],
                               [(0, 0), (1, 0), (2, 0), (2, 1)], [(1, 0), (1, 1), (1, 2), (0, 2)]],
                              [[(0, 1), (1, 1), (2, 1), (2, 0)], [(0, 0), (0, 1), (0, 2), (1, 2)],
                               [(0, 0), (0, 1), (1, 0), (2, 0)], [(0, 0), (1, 0), (1, 1), (1, 2)]],
                              [[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)],
                               [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)]],
                              [[(0, 0), (0, 1), (1, 1), (1, 0)], [(0, 0), (0, 1), (1, 1), (1, 0)],
                               [(0, 0), (0, 1), (1, 1), (1, 0)], [(0, 0), (0, 1), (1, 1), (1, 0)]],
                              [[(0, 1), (1, 1), (1, 0), (2, 0)], [(0, 0), (0, 1), (1, 1), (1, 2)],
                               [(0, 1), (1, 1), (1, 0), (2, 0)], [(0, 0), (0, 1), (1, 1), (1, 2)]],
                              [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)],
                               [(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (1, 1), (0, 1), (0, 2)]],
                              [[(1, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 1)],
                               [(0, 0), (1, 0), (2, 0), (1, 1)], [(1, 0), (1, 1), (1, 2), (0, 1)]]][i_]
        self.color = self.colors[i_]
        self.cords = self.cords_rotates[0]
        self.pos = [4, 0]
        if i_ == 2:
            self.pos = [3, 0]

    def rotate(self, colors):
        i_ = self.cords_rotates.index(self.cords)
        if i_ == 3:
            i_ = 0
        else:
            i_ += 1

        flag = True
        for a_ in self.cords_rotates[i_]:
            if (self.pos[0] + a_[0] >= 10) or (self.pos[1] + a_[1] >= 20):
                flag = False
            elif colors[(self.pos[0] + a_[0], self.pos[1] + a_[1])] is not None:
                flag = False
        if flag:
            self.cords = self.cords_rotates[i_]

    def move(self, colors, direction):
        flag = True
        if direction == 0:
            for cord in self.cords:
                if self.pos[0] + cord[0] + 1 > 9:
                    flag = False
                elif colors[(self.pos[0] + cord[0] + 1, self.pos[1] + cord[1])] is not None:
                    flag = False
            if flag:
                self.pos[0] += 1

        elif direction == 1:
            for cord in self.cords:
                if self.pos[1] + cord[1] + 1 > 19:
                    flag = False
                elif colors[(self.pos[0] + cord[0], self.pos[1] + cord[1] + 1)] is not None:
                    flag = False
            if flag:
                self.pos[1] += 1
            else:
                return False
        elif direction == 2:
            if self.pos[0] < 1:
                flag = False
            else:
                for cord in self.cords:
                    if colors[(self.pos[0] + cord[0] - 1, self.pos[1] + cord[1])] is not None:
                        flag = False
            if flag:
                self.pos[0] -= 1
        return True
