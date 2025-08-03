from constants import *

class Helicopter:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.water = 0
        self.max_water = 1

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def action(self, map_obj):
        cell = map_obj.grid[self.y][self.x]
        if cell == WATER:
            self.water = self.max_water
        elif cell == FIRE and self.water > 0:
            map_obj.grid[self.y][self.x] = ' '
            self.water -= 1
