import random
import time
from dungeon import Dungeon, Room


class Player:
    def __init__(self):
        # for the map locatin - 2d
        self.x = 1
        self.y = 1
        self.health = 100
        self.attack = 10
        self.symbol = '$'


# class Room:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#         # create the outline of the
#         # '#' for wall, '.' for floor
#         self.map = [['#' for _ in range(w)] for _ in range(h)]
#         for y in range(1, h - 1):
#             for x in range(1, w-1):
#                 self.map[y][x] = '.'


class Game:
    def __init__(self):
        # create the room and the player
        self.dungeon = Dungeon(60, 30, max_rooms=5)
        self.player = Player()

        # Place player in the first room
        if self.dungeon.rooms:
            starting_room = self.dungeon.rooms[0]
            center_x, center_y = starting_room.center()
            self.player.x = center_x
            self.player.y = center_y

        self.is_running = True
        # print("\033[H\033[J", end="")

    def display(self):
        # \033[H moves the cursor to the top-left position and
        # \033[J clears the screen from the cursor position to the end

        print("\033[H\033[J", end="")
        for y in range(self.dungeon.height):
            for x in range(self.dungeon.width):
                if x == self.player.x and y == self.player.y:
                    print(self.player.symbol, end='')
                else:
                    print(self.dungeon.map[y][x], end='')
            print()

        print(f"Your Health: {self.player.health}")

    def input(self):
        move = input(
            "Move: w - up, s - down, a - left, d - right. q - for quit\n").lower()
        m_x, m_y = 0, 0

        if move == 'w':
            m_y = -1
        elif move == 's':
            m_y = 1
        elif move == 'a':
            m_x = -1
        elif move == 'd':
            m_x = 1
        elif move == 'q':
            self.is_running = False

        new_x = self.player.x + m_x
        new_y = self.player.y + m_y

        if self.dungeon.map[new_y][new_x] != '#':
            self.player.x = new_x
            self.player.y = new_y

    def run(self):
        while self.is_running:
            self.display()
            self.input()


if __name__ == "__main__":
    print("=================")
    print("Welcome to Rogue-lite Dungeon Crawler game!")
    print("Goodluck")
    time.sleep(3)
    game = Game()
    game.run()
