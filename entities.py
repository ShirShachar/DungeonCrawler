import random


class Enemy:
    def __init__(self, x, y, symbol='E', name="Enemy", health=20, attack=5, can_shoot=False):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name
        self.health = health
        self.attck = attack
        self.can_shoot = can_shoot
        self.fireball_range = 5  # Maximum range for fireballs
        self.fireball_damage = 15  # Damage dealt by fireballs
        self.fireball_cooldown = 0  # Cooldown counter for fireball attacks
        self.max_cooldown = 3  # Number of turns to wait between fireball attacks

    def move_towards(self, target_x, target_y, dungeon_map, occupied_positions):
        # Update cooldown counter
        if self.fireball_cooldown > 0:
            self.fireball_cooldown -= 1

        # If we can shoot and are within range, don't move
        if self.can_shoot and self.is_in_range(target_x, target_y):
            return

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

    def is_in_range(self, target_x, target_y):
        """Check if target is within fireball range and has line of sight"""
        distance = abs(target_x - self.x) + abs(target_y - self.y)
        return distance <= self.fireball_range

    def try_shoot_fireball(self, target_x, target_y, dungeon_map):
        """Attempt to shoot a fireball at the target"""
        # Check if on cooldown or can't shoot
        if not self.can_shoot or not self.is_in_range(target_x, target_y) or self.fireball_cooldown > 0:
            return None

        # 25% chance to shoot when in range and not on cooldown
        if random.random() < 0.25:
            # Set cooldown after successful shot
            self.fireball_cooldown = self.max_cooldown
            return {
                'damage': self.fireball_damage,
                'source': (self.x, self.y),
                'target': (target_x, target_y)
            }
        return None
