import random


class Enemy:
    def __init__(self, x, y, symbol='E', name="Enemy", health=20, attack=5):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name
        self.health = health
        self.attck = attack

    def move_towards(self, target_x, target_y, dungeon_map):
        d_x = 0
        if self.x < target_x:
            d_x = 1
        elif self.x > target_x:
            d_x = -1

        d_y = 0
        if self.y < target_y:
            d_y = 1
        elif self.y > target_y:
            d_y = -1

        # random pick horizontal or vertical movement first
            if random.choice([True, False]) and d_x != 0:
                if dungeon_map[self.y][self.x + d_x] == '.':
                    self.x += d_x
                elif d_y != 0 and dungeon_map[self.y + d_y][self.x] == '.':
                    self.y += d_y
            else:
                if d_y != 0 and dungeon_map[self.y + d_y][self.x] == '.':
                    self.y += d_y
                if d_x != 0 and dungeon_map[self.y][self.x + d_x] == '.':
                    self.x += d_x
