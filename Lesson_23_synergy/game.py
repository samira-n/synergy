import time
from map import Map
from helicopter import Helicopter
from utils import clear_screen

class Game:
    def __init__(self, width, height):
        self.map = Map(width, height)
        self.heli = Helicopter()
        self.score = 0
        self.tick = 0
        self.running = True

    def run(self):
        while self.running:
            clear_screen()
            self.map.update(self.tick)
            self.map.print_map(self.heli)
            print(f"Tick: {self.tick} | Score: {self.score} | Water: {self.heli.water}")
            self.handle_input()
            self.tick += 1
            time.sleep(0.3)

    def handle_input(self):
        import msvcrt  # работает на Windows
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w':
                self.heli.move(0, -1)
            elif key == 's':
                self.heli.move(0, 1)
            elif key == 'a':
                self.heli.move(-1, 0)
            elif key == 'd':
                self.heli.move(1, 0)
            elif key == ' ':
                self.heli.action(self.map)
            elif key == 'q':
                self.running = False
