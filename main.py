from time import sleep
from item import *
from book import *
import re
# Classes

class Room:
    def __init__(self, room_id, name, description, north_exit=None, south_exit=None, east_exit=None, west_exit=None, up_exit=None, down_exit=None, on_entrance=None, on_exit=None, items=None): # It's a constructor, init?
        self.north_exit = north_exit
        self.south_exit = south_exit
        self.east_exit = east_exit
        self.west_exit = west_exit
        self.up_exit = up_exit
        self.down_exit = down_exit
        self.name = name
        self.description = description
        self.room_id = room_id
        self.explored = False
        self.on_entrance = on_entrance if on_entrance is not None else lambda exit_id: self.default_on_entrance(exit_id)
        self.on_exit = on_exit if on_exit is not None else lambda exit_id: self.default_on_exit(exit_id)
        self.items = items if items is not None else []

    def default_on_entrance(self, exit_id):
        for i in self.items:
            if i.name[0].lower() in 'aeiou':
                print("There is an " + i.name + " here.")
            else:
                print("There is a " + i.name + " here.")

    def default_on_exit(self, exit_id):
        pass
    
    def move(self, exit_id): 
        global current_room
        if exit_id == "n":
            if self.north_exit is not None:
                current_room = self.north_exit
                self.on_exit(exit_id)
                rooms[current_room].on_entrance(exit_id)
                return True
            else:
                print("You cannot go that way")
                return False
        elif exit_id == "s":
            if self.south_exit is not None:
                current_room = self.south_exit
                self.on_exit(exit_id)
                rooms[current_room].on_entrance(exit_id)
                return True
            else:
                print("You cannot go that way")
                return False
        elif exit_id == "e":
            if self.east_exit is not None:
                current_room = self.east_exit
                self.on_exit(exit_id)
                rooms[current_room].on_entrance(exit_id)
                return True
            else:
                print("You cannot go that way")
                return False
        elif exit_id == "w":
            if self.west_exit is not None:
                current_room = self.west_exit
                self.on_exit(exit_id)
                rooms[current_room].on_entrance(exit_id)
                return True
            else:
                print("You cannot go that way")
                return False
        elif exit_id == "u":
            if self.up_exit is not None:
                current_room = self.up_exit
                self.on_exit(exit_id)
                rooms[current_room].on_entrance(exit_id)
                return True
            else:
                print("You cannot go that way")
                return False
        elif exit_id == "d":
            if self.down_exit is not None:
                current_room = self.down_exit
                self.on_exit(exit_id)
                rooms[current_room].on_entrance(exit_id)
                return True
            else:
                print("You cannot go that way")
                return False
        else:
            print("What was that?")
    
    def getItemWithClass(self, item_name, class_=(Item,)):
        for i in self.items:
            if i.name == item_name and isinstance(i, class_):
                return i
        return None

    def getItemsOfClass(self, class_):
        results_of_search = []
        for i in self.items:
            if isinstance(i, class_):
                results_of_search.append(i)
        return results_of_search

    def getItem(self, item_name):
        for i in self.items:
            if i.name == item_name:
                return i
        return None

    def removeItem(self, item_name):
        item = self.getItem(item_name)
        if item:
            self.items.remove(item)
            return item
        return None

COMMAND_PATTERNS = {
    r"^(n|north|go north)$": "move_north",
    r"^(s|south|go south)$": "move_south",
    r"^(e|east|go east)$": "move_east",
    r"^(w|west|go west)$": "move_west",
    r"^(u|up|go up)$": "move_up",
    r"^(d|down|go down)$": "move_down",
    r"^(look)$": "look",
    r"^look at (.+)$": "look_at",
    r"^(h|help)$": "help",
    r"^help (.+)$": "help_with",
    r"^(i|inventory|take inventory)$": "take_inventory",
    r"^take ((?:(?! and ).)+)(?: and ((?:(?! and ).)+))?(?: and ((?:(?! and ).)+))?$": "take",
    r"^drop ((?:(?! and ).)+)(?: and ((?:(?! and ).)+))?(?: and ((?:(?! and ).)+))?$": "drop",
    r"^read (.+?)(?: page (\d+))?$": "read"

} # I'll admit that I got a lot of help here from ChatGPT; I HATE Regex, but it was the only way to get what I wanted to accomplish. I hope that you allow this.

def move_north():
    if rooms[current_room].move("n"):  # Check if the move is possible. The move function that I made returns True if you can successfully move. 
        print(rooms[current_room].name)
        if not rooms[current_room].explored:
            print(rooms[current_room].description)
            rooms[current_room].explored = True
def move_south():
    if rooms[current_room].move("s"):
        print(rooms[current_room].name)
        if not rooms[current_room].explored:
            print(rooms[current_room].description)
            rooms[current_room].explored = True
def move_east():
    if rooms[current_room].move("e"):
        print(rooms[current_room].name)
        if not rooms[current_room].explored:
            print(rooms[current_room].description)
            rooms[current_room].explored = True
def move_west():
    if rooms[current_room].move("w"):
        print(rooms[current_room].name)
        if not rooms[current_room].explored:
            print(rooms[current_room].description)
            rooms[current_room].explored = True
def move_up():
    if rooms[current_room].move("u"):
        print(rooms[current_room].name)
        if not rooms[current_room].explored:
            print(rooms[current_room].description)
            rooms[current_room].explored = True
def move_down():
    if rooms[current_room].move("d"):
        print(rooms[current_room].name)
        if not rooms[current_room].explored:
            print(rooms[current_room].description)
            rooms[current_room].explored = True

def look():
    print(rooms[current_room].description)
    item_list = []
    item_list.extend(rooms[current_room].items)
    item_list.extend(inventory)
    for i in item_list:
            if i.name[0].lower() in 'aeiou':
                print("There is an " + i.name + " here.")
            else:
                print("There is a " + i.name + " here.")
def look_at(item):
    global rooms
    global current_room
    item_list = []
    item_list.extend(rooms[current_room].items)
    item_list.extend(inventory)
    for i in item_list:
        if i.name == item:
            print(i.description)
            return
    else:
        print("What?")

def take(*item_names):
    global rooms
    global current_room
    global inventory
    

    items = []
    items.extend(rooms[current_room].items)

    for item_name in item_names:
        found = False
        for i in items:
            if i.name == item_name and not i.fixed:

                inventory.append(i)
                rooms[current_room].items.remove(i)
                found = True
                print("You took the " + item_name)
                break
            elif i.name == item_name and i.fixed:
                found = True
                print("The " + item_name + " is immovable, much less pocketable.")
                break
        
        # If the item wasn't found
        if not found:
            print("No item was found with this name: " + item_name)
def drop(*item_names):
    global rooms
    global current_room
    global inventory

    items = []
    items.extend(inventory)

    for item_name in item_names:
        found = False
        for i in items:
            if i.name == item_name:
                rooms[current_room].items.append(i)
                inventory.remove(i)
                found = True
                print("You dropped the " + item_name)
                break
        
        if not found:
            print("No item was found with this name: " + item_name)

def read(item_name, page):
    global rooms
    global inventory
    global current_room
    item_list = []
    item_list.extend(rooms[current_room].getItemsOfClass(Inscription)) # Get all written text objects from surrounding room
    item_list.extend(inventory) # And then get everything in the inventory. TODO: Make inventory into a class with getters and setters
    for i in item_list:
        if i.name == item_name:
            if page == None:
                page = 1
            page = int(page) - 1
            print(i.get_page(page))
            return
    print("Didn't find that book")

def take_inventory():
    global rooms
    global current_room
    global inventory

    items = []
    items.extend(inventory)
    print("You have the following items: ")
    for i in items:
        print(i.name)

def help():
    print("Available commands:")
    print("  n, north, go north         - Move north")
    print("  s, south, go south         - Move south")
    print("  e, east, go east           - Move east")
    print("  w, west, go west           - Move west")
    print("  u, up, go up               - Move up")
    print("  d, down, go down           - Move down")
    print("  look                       - Look around the room")
    print("  look at <item>             - Look at a specific item")
    print("  h, help                    - Show this help message")
    print("  help <command>             - Get help on a specific command")
    print("  take <item>                - Take item from room")
    print("  drop <item>                - Drop item from inventory")
    print("  read <item> [page <num>]   - Read page of item")
    print("  i, inventory               - Take inventory")
def help_with(command):
    command_help = {
        "north": "Use 'north' or 'n' to move north.",
        "south": "Use 'south' or 's' to move south.",
        "east": "Use 'east' or 'e' to move east.",
        "west": "Use 'west' or 'w' to move west.",
        "up": "Use 'up' or 'u' to move up.",
        "down": "Use 'down' or 'd' to move down.",
        "look": "Use 'look' to see details about the current room.",
        "look at": "Use 'look at <item>' to see details about a specific item.",
        "help": "Use 'help' to see a list of commands, or 'help <command>' to learn about a specific command.",
        "take": "Use 'take <item>' to take an item from the room if it isn't fixed there.",
        "drop": "Use 'drop <item>' to drop and item from your inventory.",
        "read": "Use 'read <item>' to read an item. You can also specify page number with 'read <item> page <num>'.",
        "inventory": "Use 'i' or 'inventory' or 'take inventory' to take inventory of your current items"

    }
    print(command_help.get(command, "No help available for that command.")) # dictionary functions are so useful!

# Variables

rooms = [
    # Outside Rooms
    Room(0, "Green Field", "You stand in an open field facing north, with grassy expanses to the left and to the right, and a thorny forest to your back. A white house stands serenely to your north", north_exit=1, east_exit=8, west_exit=2, items=[Item("rock", "It is a pebble of a rock", fixed=False),Item("big rock", "It is a boulder of a rock", fixed=True)]),
    Room(1, "The Front Yard", "You are now standing in the unfenced and overgrown front yard of the white house, with the green field you woke up in south of you. You are facing the door, which is north of you.", north_exit=12, south_exit=0, east_exit=7, west_exit=3),
    Room(2, "Green Field", "You are now in a green field, with the thorny forest blocking your path both west and south. There is more field to the north and to the east.", north_exit=3, east_exit=0),
    Room(3, "Green Field", "You are now in a green field west of the house. Your path is blocked by thorny forests to the west, but are otherwise unhindered.", north_exit=4, east_exit=1, south_exit=2),
    Room(4, "Green Field", "You are now in a green field northwest of the house, with more fields to the south and the east.", east_exit=5, south_exit=3),
    Room(5, "Forest Entrance", "You are behind the house at the forest entrance, with green fields to your left and your right, and an old forest ahead, north of you.", west_exit=4, north_exit=9, east_exit=6),
    Room(6, "Green Field", "You are now northeast of the house in a green field, with the paths north and east blocked off by a thorny forest. Other than that, you are unhindered.", west_exit=5, south_exit=7),
    Room(7, "Green Field", "You are now east of the house. There are more grassy expanses north and south.", north_exit=6, south_exit=8, west_exit=1),
    Room(8, "Green Field", "You are now southeast of the house in a grassy field bathed in sunlight, and you can see grassy expanses to the west and to the north.", north_exit=7, west_exit=0),
    Room(9, "Forest Entrance", "You are now on the bounderies of the thorny forest. You can either go south to the grassy fields with the house behind you, or you can go north deeper into the forest.", north_exit=10, south_exit=5),
    Room(10, "Forest Path", "You are now on a narrow forest path, leading west towards an ominously dark clearing next to a cliffside. South of you is the path to the forest entrance.", south_exit=9, west_exit=11),
    Room(11, "Cave Entrance", "You are now in the clearing close to the entrance of the cave. You may choose to go into the cave westwards, or you may go into the forest east towards the white house.", east_exit=10, west_exit=26),
    Room(12, "Living Room", "You are in the living room of a small white house, with the door to your south, the dining room to your north, and the stairs to the east.", south_exit=1, east_exit=15, north_exit=13, items=[dirty_page, holy_book]),
    Room(13, "Dining Room", "You are in the dining room of a small house, with the kitchen to your east and the living room to your south.", east_exit=14, south_exit=12),
    Room(14, "Kitchen", "You are now in the kitchen, with the stairs to the south and the dining room to the west", south_exit=15, west_exit=13),
    Room(15, "Stairs", "You are now on the stairwell. You can choose to go up or down, or go north to the kitchen or west to the living room.", north_exit=14, west_exit=12, up_exit=19, down_exit=16),
    Room(16, "Stairs", "You are at the bottom of a stairwell, and you can either choose to go up the stairs or go north to enter the boiler room.", up_exit=15, north_exit=17),
    Room(17, "Boiler Room", "You are in the boiler room, with the entrance to the stairwell south of you and the cellar to the west.", west_exit=18, south_exit=16),
    Room(18, "Cellar", "You are now in the cellar, with the boiler room to the east. You see a ladder going down into a dark cave.", down_exit=23, east_exit=17),
    Room(19, "Stairs", "You are now at the top of a stairwell, with the office behind a door to the north and a bedroom to the west.", down_exit=15, west_exit=22, north_exit=20),
    Room(20, "Office", "You are standing in the office. There is a stairway to the south and the bathroom to the west.", west_exit=21, south_exit=19, items=[sample_book]),
    Room(21, "Bathroom","You are standing in the restroom. There are two doors, one leading to the office eastward, and the other leading south to the bedroom.", east_exit=20, south_exit=22),
    Room(22, "Bedroom","You are standing in the bedroom. There is a door leading east to the stairs and a door going north into the bathroom.", east_exit=19, north_exit=21),
    Room(23, "Cave Chamber","You are in a small chamber in a cave, with a passageway leading north. A ladder leads up to a cellar.", up_exit=18, north_exit=24),
    Room(24, "Cave Tunnel", "You are in a dark and damp passageway, with a chamber south of you and more tunnel north of you.", south_exit=23, north_exit=25),
    Room(25, "Cave Tunnel", "You are in a dark and damp passageway, with more tunnel south and a chamber north of you.", south_exit=24, north_exit=26),
    Room(26, "Cave Chamber", "You are now in a large chamber with a crack east of you, and a tunnel south.", south_exit=25, east_exit=11)
] # A veritable spaghetti of code

current_room = 0
inventory = []

# Game setup
welcome_string = """
****************************************** 
*           _             _____          * 
*          | | ___ __ ___/ _  /          * 
*          | |/ / '__/ _ \// /           * 
*          |   <| | | (_) / //\          * 
*          |_|\_\_|  \___/____/          * 
*                                        *
*         a text adventure game          *
*                                        *
****************************************** 
"""

print(welcome_string)
sleep(2)
print(rooms[current_room].name)
print(rooms[current_room].description)
rooms[current_room].on_entrance("n")
rooms[current_room].explored = True
print("Type h or help to get help")

# Command processing function, by ChatGPT cause ReGeX is impossible. 
def handle_command(command):
    for pattern, handler_name in COMMAND_PATTERNS.items():
        match = re.match(pattern, command, re.IGNORECASE)
        if match:
            handler = globals().get(handler_name)
            if handler:
                try:
                    # Check if any capture groups exist (non-empty tuple) before passing
                    if len(match.groups()) > 0:
                        handler(*match.groups())
                    else:
                        handler()
                except TypeError as e:
                    handler() # Cause the else statement doesn't seem to catch it well.
            return
    print("Unknown command.")


# Game loop

while True:
    prompt = str.lower(input(">>> "))
    prompt = prompt if prompt != None else "null boi" # It's a null, boi
    prompt = prompt if prompt != "" else "null boi"
    handle_command(prompt)