# this is for the rooms
import random


class Room:
    def __init__(self, x, y, w, h):
        self.x = x  # this is x for the top left corner position
        self.y = y  # this is y for the top left corner position
        self.width = w
        self.height = y
        self.is_connected = False  # is the room connected to anothe one

    def intersects(self, other_room, padding=1):
        # Check if this room intersects with another room
        return (self.x - padding < other_room.x + other_room.width and
                self.x + self.width + padding > other_room.x and
                self.y - padding < other_room.y + other_room.height and
                self.y + self.height + padding > other_room.y)

    def center(self):
        center_x = int(self.x + self.width / 2)
        center_y = int(self.y + self.height / 2)
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
        for _ in range(self.max_rooms):
            # width and height of the room
            w = random.randint(self.room_min_size, self.room_max_size)
            h = random.randint(self.room_min_size, self.room_max_size)

            # postion x and y - to make sure were not out of boundraies
            x = random.randint(1, self.width - w - 1)
            y = random.randint(1, self.height - h - 1)

            new_room = Room(x, y, w, h)

            failed_to_make_room = False
            for other_room in self.rooms:
                if new_room.intersects(other_room):
                    failed_to_make_room = True
                    break

            if not failed_to_make_room:
                self.create_room(new_room)

                # Connect to the previous room
                if len(self.rooms) > 0:
                    # Center coordinates of new room and previous room
                    (new_x, new_y) = new_room.center()
                    (prev_x, prev_y) = self.rooms[-1].center()

                    # Connect with horizontal and vertical tunnels
                    if random.randint(0, 1) == 1:
                        # First horizontal, then vertical
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # First vertical, then horizontal
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                    # Mark the room as connected
                    new_room.connected = True
                    self.rooms[-1].connected = True

                # Add the new room to the list
                self.rooms.append(new_room)

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
