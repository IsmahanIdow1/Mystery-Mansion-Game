from items import *

room_grandhall = {
    "name": "The GrandHall",

    "description":
    """You are currently standing in a dark barely lit hall of the abandoned mansion. 
    There is cobwebs everywhere around you. The air is thick and feels like it is wrapping around you.
    A vase staircase awaits for your present and a note reads: "This key is the beginning
    of something far greater... and far darker...
    Corridors lead north and east.""",

     "exits": {"north": "library", "east": "diningroom"},

    "items": [item_note]
}

room_library = {
    "name": "The library",

    "description":
    """You are currently in the Library.
    Rows of acient books sat silently, theirs spines cracked and faded,
   as if they are silently judging you.
    Dust loomed every corner as though it was hiding something.
   The sent of mold thicken the room.
    On a warped wooden table lies an open journal. Ink circled in black marked: 
    "The key is hidden where no meal was ever served..."
    Somewhere in the silence, a faint whisper echoed.
    Door leads east and south, but the darkness seem to follow itself..""",

    "exits": {"south": "grandhall", "east": "study"},

    "items": [item_journal, item_candle]
}

room_study = {
    "name": "The Study",

    "description":
    """You are in the study. The broken clock
    ticks hoping to be fixed, stuck at three am,
    A drawer is locked tight seeming as though something is being hidden.
    You can return west to the Library or go south to the Dining room""",
 
"exits": {"west": "library", "south": "diningroom"},

    "items": [item_latern]
}

room_diningroom = {
    "name": "The Dining Room",

    "description":
    """You are standing in the DiningRoom. A table sits covered in cobwebs.
    Plates and glasses remain like how they last were, poisoning any nose that
    went a mile near. Beneath the table, stares a faint SILVER KEY half
    out in the open covered in mold.
    You can go west to the Grand Hall, north to the Study, and east to the Kitchen.""",

   "exits": {"west": "grandhall", "north": "study", "east": "kitchen"},

    "items": [item_silverkey]
}

room_kitchen = {
    "name": "The Kitchen",

    "description":
    """You are now in the Kitchen. Rust and decay effect the air.
    Dusty pots hang above the stove turning cold.
    Its lock glints, shaped for a silver key.
    You can go west to the Dining Room or down to the Cellar.""",

   "exits": {"west": "diningroom", "down": "cellar"},
    
   "items": []
}

room_cellar = {
    "name": "The Cellar",

    "description":
    """You are now in the cellar. Cold, damp air sticks to you.
    The truth causes hairs to stick up: the mansion's last presents
    never left.
    Stairs lead bak up to the Kitchen.""",

    "exits": {"up": "kitchen"},

    "items": []
}

rooms = {
    "grandhall": room_grandhall,
    "library": room_library,
    "study": room_study,
    "diningroom": room_diningroom,
    "kitchen": room_kitchen,
    "cellar": room_cellar

}