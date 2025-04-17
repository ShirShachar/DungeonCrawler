import random
import time
from entities import Enemy
from dungeon import Dungeon, Room
from items import Item


class Player:
    def __init__(self):
        # for the map locatin - 2d
        self.x = 1
        self.y = 1
        self.health = 100
        self.attack = 10
        self.symbol = '$'


class Game:
    def __init__(self):
        # create the room and the player
        self.dungeon = Dungeon(60, 30, max_rooms=5)
        self.player = Player()
        # for health
        self.items = []
        self.inventory = []
        self.populate_items()

        # Place player in the first room
        if self.dungeon.rooms:
            starting_room = self.dungeon.rooms[0]
            center_x, center_y = starting_room.center()
            self.player.x = center_x
            self.player.y = center_y

        self.enemies = []
        self.populate_enemies()

        self.is_running = True
        # print("\033[H\033[J", end="")

    def populate_items(self):
        for room in self.dungeon.rooms[1:]:
            if random.random() < 0.5:  # 50% chance
                x = random.randint(room.x + 1, room.x + room.width - 2)
                y = random.randint(room.y + 1, room.y + room.height - 2)
                if self.dungeon.map[y][x] == '.':
                    self.items.append(Item(x, y))

    def populate_enemies(self):
        # Define enemy types
        enemy_types = [
            {'name': 'Goblin', 'symbol': 'G', 'health': 15, 'attack': 3},
            {'name': 'Orc', 'symbol': 'O', 'health': 30, 'attack': 7},
            {'name': 'Slime', 'symbol': 'S', 'health': 10, 'attack': 2}
        ]

        # Place enemies in rooms (skip first room)
        if len(self.dungeon.rooms) > 1:
            for room in self.dungeon.rooms[1:]:
                n_enemies = random.randint(1, 3)
                for _ in range(n_enemies):
                    x = random.randint(room.x + 1, room.x + room.width - 2)
                    y = random.randint(room.y + 1, room.y + room.height - 2)

                    if 0 <= x < self.dungeon.width and 0 <= y < self.dungeon.height:
                        if self.dungeon.map[y][x] == '.':
                            et = random.choice(enemy_types)
                            self.enemies.append(
                                Enemy(x, y, et['symbol'], et['name'],
                                      et['health'], et['attack'])
                            )
                            print(
                                f"Room: x={room.x}, y={room.y}, width={room.width}, height={room.height}")
                            print(
                                f"Map dimensions: {self.dungeon.width}x{self.dungeon.height}")
                            print(f"Trying to place enemy at: x={x}, y={y}")
                            break

    def display(self):
        # \033[H moves the cursor to the top-left position and
        # \033[J clears the screen from the cursor position to the end

        print("\033[H\033[J", end="")
        display_map = [row[:] for row in self.dungeon.map]

        # Add enemies
        for enemy in self.enemies:
            display_map[enemy.y][enemy.x] = enemy.symbol

        for y in range(self.dungeon.height):
            for x in range(self.dungeon.width):
                if x == self.player.x and y == self.player.y:
                    print(self.player.symbol, end='')
                else:
                    print(display_map[y][x], end='')
            print()

        for item in self.items:
            display_map[item.y][item.x] = item.symbol

        print(f"Your Health: {self.player.health}")
        print(f"Enemies remaining: {len(self.enemies)}")

    def enemies_move(self):
        occupied = {(e.x, e.y) for e in self.enemies if e.health > 0}
        occupied.add((self.player.x, self.player.y))

        # Create a copy of the enemy list to avoid modification issues
        for e in list(self.enemies):
            pos = (e.x, e.y)
            if pos in occupied:
                occupied.remove(pos)

            # If enemy is adjacent to player, attack
            if abs(e.x - self.player.x) + abs(e.y - self.player.y) == 1:
                print(f"{e.name} attacks you for {e.attck} damage!")
                self.player.health -= e.attck
            else:
                e.move_towards(self.player.x, self.player.y,
                               self.dungeon.map, occupied)

            occupied.add((e.x, e.y))  # re-add their new position

    def attack_enemy(self):
        for e in self.enemies:
            if abs(e.x - self.player.x) + abs(e.y - self.player.y) == 1:
                print(f"You hit {e.name} for {self.player.attack} damage!")
                e.health -= self.player.attack
                if e.health <= 0:
                    print(f"You defeated {e.name}!")
                    self.enemies.remove(e)
                break
        else:
            print("No enemy nearby to attack.")

    def input(self):
        move = input(
            "Move: w - up, s - down, a - left, d - right. f - attack. q - quit\n").lower()
        m_x, m_y = 0, 0

        if move == 'w':
            m_y = -1
        elif move == 's':
            m_y = 1
        elif move == 'a':
            m_x = -1
        elif move == 'd':
            m_x = 1
        elif move == 'f':
            self.attack_enemy()
            return
        elif move == 'u':
            for item in self.inventory:
                if item.effect == 'heal':
                    self.player.health = min(
                        100, self.player.health + item.value)
                    print(f"You used a {item.name}! Healed {item.value} HP.")
                    self.inventory.remove(item)
                    break
            else:
                print("You have no health potions!")
        elif move == 'q':
            self.is_running = False
            return

        new_x = self.player.x + m_x
        new_y = self.player.y + m_y

        if self.dungeon.map[new_y][new_x] != '#':
            self.player.x = new_x
            self.player.y = new_y

        if move in ['w', 'a', 's', 'd']:
            self.enemies_move()

    def run(self):
        while self.is_running and self.player.health > 0 and len(self.enemies) > 0:
            self.display()
            self.input()

        self.display()

        if self.player.health <= 0:
            print("\nGame Over! You died 💀")
        elif len(self.enemies) == 0:
            print("\n🎉 You defeated all the enemies! You win!")
            choice = input("Do you want to play again? (y/n): ").lower()
            if choice == 'y':
                self.__init__()
                self.run()
            else:
                print("Thanks for playing!")
        else:
            print("You quit the game.")


if __name__ == "__main__":
    print("=================")
    print("Welcome to Rogue-lite Dungeon Crawler game!")
    print("Goodluck")
    time.sleep(3)
    game = Game()
    game.run()
