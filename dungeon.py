# this is for the rooms
import random


class Room:
    def __init__(self, x, y, w, h):
        self.x = x  # this is x for the top left corner position
        self.y = y  # this is y for the top left corner position
        self.width = w
        self.height = y
        self.is_connected = False  # is the room connected to anothe one


class Dungeon:
    def __init__(self, w, h, max_rooms, room_min_size, roim_max_size):
        self.width = w
        self.height = h
        self.max_rooms = 10
        self.room_min_size = 5
        self.room_max_size = 10

        self.map = [['#' for _ in range(w)] for _ in range(h)]
        self.rooms = []
