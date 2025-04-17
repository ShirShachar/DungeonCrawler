import random


class Enemy:
    def __init__(self, x, y, symbol='E', name="Enemy", health=20, attack=5):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name
        self.health = health
        self.attck = attack

    def move_towards(self, target_x, target_y, dungeon_map, occupied_positions):
        dx = target_x - self.x
        dy = target_y - self.y

        step_x = 1 if dx > 0 else -1 if dx < 0 else 0
        step_y = 1 if dy > 0 else -1 if dy < 0 else 0

        # Try horizontal move
        new_x = self.x + step_x
        new_y = self.y

        if (new_x, new_y) not in occupied_positions and dungeon_map[new_y][new_x] == '.':
            self.x = new_x
            self.y = new_y
            return

        # Try vertical move
        new_x = self.x
        new_y = self.y + step_y

        if (new_x, new_y) not in occupied_positions and dungeon_map[new_y][new_x] == '.':
            self.x = new_x
            self.y = new_y
