# this is for the rooms
import random


class Room:
    def __init__(self, x, y, w, h):
        self.x = x  # this is x for the top left corner position
        self.y = y  # this is y for the top left corner position
        self.width = w
        self.height = h
        self.is_connected = False  # is the room connected to anothe one

    def intersects(self, other_room, padding=1):
        # Check if this room intersects with another room
        return (self.x - padding < other_room.x + other_room.width and
                self.x + self.width + padding > other_room.x and
                self.y - padding < other_room.y + other_room.height and
                self.y + self.height + padding > other_room.y)

    def center(self):
        center_x = int(self.x + self.width // 2)
        center_y = int(self.y + self.height // 2)
        return (center_x, center_y)


class Dungeon:
    def __init__(self, w, h, max_rooms=10, room_min_size=5, roim_max_size=10):
        self.width = w
        self.height = h
        self.max_rooms = 10
        self.room_min_size = 5
        self.room_max_size = 10

        self.map = [['#' for _ in range(w)] for _ in range(h)]
        self.rooms = []

        self.generate()

    def create_room(self, room):
        # Create a rectangular room
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.map[y][x] = '.'

    def generate(self):
        attempts = 0

        while len(self.rooms) < self.max_rooms and attempts < self.max_rooms * 5:
            attempts += 1

            # Room size with limits
            w = random.randint(self.room_min_size, self.room_max_size)
            h = random.randint(self.room_min_size, self.room_max_size)

            # Avoid weird skinny rooms
            if h > w * 2:
                h = w
            if w > h * 2:
                w = h

            # Position inside map bounds (leave 1 tile buffer)
            x = random.randint(1, self.width - w - 2)
            y = random.randint(1, self.height - h - 2)

            new_room = Room(x, y, w, h)

            # Skip if overlapping
            if any(new_room.intersects(other) for other in self.rooms):
                continue

            # Carve the room
            self.create_room(new_room)

            # Connect to previous room
            if self.rooms:
                new_x, new_y = new_room.center()
                prev_x, prev_y = self.rooms[-1].center()

                if random.randint(0, 1):
                    self.create_h_tunnel(prev_x, new_x, prev_y)
                    self.create_v_tunnel(prev_y, new_y, new_x)
                else:
                    self.create_v_tunnel(prev_y, new_y, prev_x)
                    self.create_h_tunnel(prev_x, new_x, new_y)

                new_room.is_connected = True
                self.rooms[-1].is_connected = True

            self.rooms.append(new_room)

            print(f"Generated {len(self.rooms)} rooms.")

    def create_h_tunnel(self, x1, x2, y):
        # Create a horizontal tunnel
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= x < self.width and 0 <= y < self.height:
                self.map[y][x] = '.'

    def create_v_tunnel(self, y1, y2, x):
        # Create a vertical tunnel
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= x < self.width and 0 <= y < self.height:
                self.map[y][x] = '.'

    def get_random_room(self):
        # Return a random room
        if self.rooms:
            return random.choice(self.rooms)
        return None

    def print_map(self):
        # Print the map for debugging
        for row in self.map:
            print(''.join(row))


# Example usage
if __name__ == "__main__":
    dungeon = Dungeon(80, 40, max_rooms=10)
    dungeon.print_map()
    print(f"Generated {len(dungeon.rooms)} rooms")
