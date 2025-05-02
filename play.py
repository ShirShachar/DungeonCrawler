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
    def __init__(self, level=1):
        self.level = level
        # Level-specific settings
        if level == 1:
            width, height = 40, 30
            self.enemy_count = 3
        elif level == 2:
            width, height = 40, 30
            self.enemy_count = 4
        elif level == 3:
            width, height = 60, 40
            self.enemy_count = 5
        elif level == 4:
            width, height = 80, 50
            self.enemy_count = 7
        else:  # level 5
            width, height = 80, 50
            self.enemy_count = 8

        # create the room and the player with level-specific size
        self.dungeon = Dungeon(width, height, max_rooms=3 + level)
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
        # Base chance is 40%, increases slightly with level
        base_chance = 0.4
        spawn_chance = min(base_chance + (self.level - 1) * 0.1, 0.7)

        # Minimum and maximum items per level
        min_items = 1
        max_items = self.level + 1

        items_placed = 0
        rooms = self.dungeon.rooms[1:]  # Skip first room
        random.shuffle(rooms)  # Randomize room order

        # Ensure at least one item is placed
        for room in rooms:
            if items_placed >= min_items:
                break

            x = random.randint(room.x + 1, room.x + room.width - 2)
            y = random.randint(room.y + 1, room.y + room.height - 2)
            if self.dungeon.map[y][x] == '.':
                self.items.append(Item(x, y))
                items_placed += 1

        # Try to place additional items
        for room in rooms:
            if items_placed >= max_items:
                break

            if random.random() < spawn_chance:
                x = random.randint(room.x + 1, room.x + room.width - 2)
                y = random.randint(room.y + 1, room.y + room.height - 2)
                if self.dungeon.map[y][x] == '.':
                    self.items.append(Item(x, y))
                    items_placed += 1

    def populate_enemies(self):
        # Define enemy types
        enemy_types = [
            {'name': 'Goblin', 'symbol': 'G', 'health': 15,
                'attack': 3, 'can_shoot': False},
            {'name': 'Orc', 'symbol': 'O', 'health': 30,
                'attack': 7, 'can_shoot': False},
            {'name': 'Slime', 'symbol': 'S', 'health': 10,
                'attack': 2, 'can_shoot': False},
            {'name': 'Wizard', 'symbol': 'W', 'health': 20, 'attack': 5,
                'can_shoot': True}  # Wizard enemy that can shoot
        ]

        # Place exactly enemy_count enemies in rooms (skip first room)
        if len(self.dungeon.rooms) > 1:
            enemies_placed = 0
            max_attempts = 100  # Prevent infinite loop
            attempts = 0
            wizard_placed = False  # Track if we've placed a wizard already

            # In higher levels (4-5), place exactly one wizard first
            if self.level >= 4 and not wizard_placed:
                # Try to place the wizard in a random room (except first room)
                for _ in range(20):  # Try a few times to place the wizard
                    room = random.choice(self.dungeon.rooms[1:])
                    x = random.randint(room.x + 1, room.x + room.width - 2)
                    y = random.randint(room.y + 1, room.y + room.height - 2)

                    if self.dungeon.map[y][x] == '.':
                        # Place the wizard
                        et = enemy_types[3]  # Wizard
                        self.enemies.append(
                            Enemy(x, y, et['symbol'], et['name'],
                                  et['health'], et['attack'], et.get('can_shoot', True))
                        )
                        enemies_placed += 1
                        wizard_placed = True
                        break

            # Place the rest of the enemies (no more wizards)
            while enemies_placed < self.enemy_count and attempts < max_attempts:
                # Try to place in a random room (except first room)
                room = random.choice(self.dungeon.rooms[1:])
                x = random.randint(room.x + 1, room.x + room.width - 2)
                y = random.randint(room.y + 1, room.y + room.height - 2)

                # Check if position is empty floor and not occupied by another enemy
                if self.dungeon.map[y][x] == '.' and not any(e.x == x and e.y == y for e in self.enemies):
                    # Choose enemy type based on level
                    if self.level <= 2:
                        et = enemy_types[2]  # Only Slimes in early levels
                    elif self.level <= 3:
                        # Goblins and Slimes in mid levels
                        et = random.choice(enemy_types[1:3])
                    else:
                        # For levels 4-5, only regular enemies (not wizards)
                        et = random.choice(enemy_types[:3])  # Other types

                    self.enemies.append(
                        Enemy(x, y, et['symbol'], et['name'],
                              et['health'], et['attack'], et.get('can_shoot', False))
                    )
                    enemies_placed += 1

                attempts += 1

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

            # Check for fireball attack first
            if e.can_shoot:
                fireball = e.try_shoot_fireball(
                    self.player.x, self.player.y, self.dungeon.map)
                if fireball:
                    self.player.health -= fireball['damage']
                    continue  # Skip normal movement/attack if fireball was shot

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
            "Move: w - up, s - down, a - left, d - right. f - attack. u - use potion. q - quit\n").lower()
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

            # Check for items at the new position
            # Create a copy of the list to modify it safely
            for item in self.items[:]:
                if item.x == self.player.x and item.y == self.player.y:
                    self.inventory.append(item)
                    self.items.remove(item)
                    print(f"Picked up {item.name}!")

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
                self.__init__(self.level + 1)
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
