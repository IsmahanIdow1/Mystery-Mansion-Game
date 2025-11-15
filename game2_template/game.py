#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).

    In the haunted corridors of the Mystery Mansion, objects howled to be recogonised
    For example:
    """

    if not items:
        return ""
    names = [item["name"] for item in items]
    return ", ".join(names)


def print_room_items(room):
    """This function takes a room as an input and displays the items found in that room,
    showing their presence in the barely lit light of the Mystery Mansion.
    If there are no items, the silence is left to the unknown.
    """

    if "items" in room and room["items"]:
        print(f"There is {list_of_items(room['items'])} here.")
    else:
        print()  # only one blank line, avoids extra


def print_inventory_items(items):
    """This function takes a list of items in the player's inventory and displays them 
    in a format helping an explorer lost in the mansion's darkness.
    """
    if items:
        print(f"You have {list_of_items(items)}")
    else:
        print("You have no items.")


def print_room(room):
    """This function takes a room as an input and ghostly displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:
    """
    print()

    print(room["name"].upper())

    print()

    print(room["description"])

    if "items" in room and room["items"]:
        print_room_items(room)
        
    print()


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:
    """
    if direction in exits:
        room_key = exits[direction]
        return rooms[room_key]["name"]
    else:
        return None

def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.  
    """
    print(f"GO {direction.upper()} to {leads_to}.")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print/*/

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Grand Hall may look like this:

    You can:
    GO NORTH to The Library.
    GO EAST to The Dining Room.
    TAKE KEY to take a sliver key.
    DROP LANTERN to drop your lantern.
    DROP JOURNAL to drop an old journal.
    Choose wisely...

    """
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print(f"TAKE {item['id'].upper()} to take {item['name']}.")

    for item in inv_items:
        print(f"DROP {item['id'].upper()} to drop {item['name']}.")
    print("Choose wisely...")

def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    """

    chosen_exi = chosen_exit.lower()
    return chosen_exit in exits
    return chosen_exit in [direction.lower() for direction in exits]


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room

    if is_valid_exit(current_room["exits"], direction):

        current_room = move(current_room["exits"], direction)
        print()
        print("You move " + direction.upper() + " into " + current_room["name"] + ".")
        print()
    else:
        print("You cannot go there.")

def execute_take(item_id):
    """Move an item from the current room to the player's inventory."""
    global inventory
    global current_room

    for item in current_room.get("items",[]):
        if item["id"] == item_id:
            inventory.append(item)
            current_room["items"].remove(item)
            print("You take " + item["name"] + ".")
            return

    print("You cannot take that.")
    
def execute_drop(item_id):
    """Moves an item from the player's inventory to the current room."""
    global inventory
    global current_room

    for item in inventory:
        if item["id"] == item_id:
            current_room.setdefault("items", []).append(item)
            inventory.remove(item)
            print("You drop " + item["name"] + ".")
            return

    print("You cannot drop that.")
    
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where? The shadow hides many ways...")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what? Be careful in what you touch...")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what? Not everything needs to be seen.")

    else:
        print("This makes no sense. The mansion hisses")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("Choose wisely... > ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    """
    if direction in exits:
        room_key = exits[direction]
        return rooms[room_key]
    else:
        return None

# This is the entry point of our program
def main():

    # Main game loop for the Mystery Mansion
    print("Welcome to the Mystery Mansion...")
    print("A breeze will attack you as you step inside...")
    print("Your goal is to find the secret within and figure a way out... if you can...")

    global current_room
    current_room = rooms["grandhall"]

    global inventory
    inventory = []
    while True:
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)

        print("DEBUG: You are in ->", current_room["name"])
        print("DEBUG: inventory ids ->", [item["id"] for item in inventory])
        if current_room["name"].lower() == "the cellar":
            has_silver_key = any(item["id"] == "silverkey" for item in inventory)
            if has_silver_key:
                print("""
You stumble into a stuffy cellar, your lantern shadows warning you to leave. 
Beneath layers of dust, faint writing catches your eyes, strange symbols
encircling a long forgotten ritual. The air grows as seconds go by,
heavy with whispers older than the mansion itself.
In the center, a half melted candle drips besides bones twisted by time.
Digging deeper, ypu uncover a seal; its markings faintly as though alive.
The hairs on your neck rises as it realizes this ritual was never meant to be uncovered.
Your lantern dims... and in the dark, the carving begin to move...
Something is alive...""")
               
                print("""
Congratulations!
You have uncovered the mansion's long hidden ritual and revealed a mystery lost to time.
The secret of the cellar are finally brought to light...
And you made it out of the Mystery Mansion; physically alive.
                """)

                print("\n--- GAME OVER ---")
                print("Thank you for playing Mystery Mansion")
                input("Press Enter to leave the darkness...")
                return

if __name__ == "__main__":
    main()