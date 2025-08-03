import random
from constants import *

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.generate_rivers()
        self.generate_trees()

    def generate_rivers(self):
        for _ in range(3):
            x = random.randint(0, self.width - 1)
            for y in range(self.height):
                self.grid[y][x] = WATER

    def generate_trees(self):
        for _ in range(self.width * self.height // 5):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] == ' ':
                self.grid[y][x] = TREE

    def update(self, tick):
        if tick % 10 == 0:
            self.random_fire()

    def random_fire(self):
        for _ in range(3):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] == TREE:
                self.grid[y][x] = FIRE

    def print_map(self, heli):
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                if (x, y) == (heli.x, heli.y):
                    row += HELI
                else:
                    row += self.grid[y][x]
            print(row)
