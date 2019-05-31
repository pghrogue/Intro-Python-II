import logging
from room import Room
from player import Player
from item import Item

from room_defs import room
from item_defs import items

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def quit_game():
    '''Exits the game gracefully, printing a goodbye message.'''
    print("Goodbye!")
    quit()


def move(player, dir):
    '''Move the player in the correct direction.

    Args:
        player (obj): The player object
        dir (str): Direction to move
    '''

    if dir == "n":
        player.move(player.location.n_to)
    elif dir == "s":
        player.move(player.location.s_to)
    elif dir == "e":
        player.move(player.location.e_to)
    elif dir == "w":
        player.move(player.location.w_to)
    else:
        exit("Error, bad direction.")
    look(player)


def look(player):
    '''Prints the room description and information to the screen.

    Args:
        player (obj): The player object
    '''

    print("\n")
    print(player.location)
    exits = player.location.get_exits()
    print("[Obvious exits: ", end=" ")
    for x in exits: print(x, end =" ")
    print("]")


def get(player, item):
    '''Checks for item in room, moves it from room to player if valid.'''
    # First check for the items in the room
    room_item = player.location.item_in_room(item)

    if room_item is not None:
        # Remove item from room if valid entry
        player.location.items.remove(room_item)

        # Add item to player if valid entry
        player.inventory.append(room_item)

        # Print message to player
        print("You get " + room_item.name)
    else:
        # Item is not in the room
        print("That is not here.")


def drop(player, item):
    '''Checks for item in player inventory, moves it from player to current room if valid.'''
    # First check for the item in the inventory
    player_item = player.item_in_inv(item)

    if player_item is not None:
        # Remove item from player if valid
        player.inventory.remove(player_item)

        # Add item to current room
        player.location.items.append(player_item)

        # Print message
        print("You drop " + item)
    else:
        # Item is not in the inventory
        print("You don't have that item to drop.")


def inv(player):
    '''Show player inventory'''
    output = "You are carrying:\n"
    items = player.items()
    
    if len(items) > 0:
        output += items
    else:
        output += "Nothing.\n"
    print(output)


def main():
    '''Entry point for the game and command loop.'''
    
    name = input("Brave adventurer! What is your name? ")
    player = Player(name.capitalize(), room['outside'])

    print(f"Welcome to your adventure, {player.name}!\n\n")
    
    look(player)

    while True:
        cmd = input("What would you like to do? ").strip()
        exits = player.location.get_exits()

        # Command loop.
        if cmd == "look" or cmd == "l":
            look(player)
        elif cmd == "quit" or cmd == "q":
            quit_game()
        elif cmd == "inventory" or cmd == "inv" or cmd == "i":
            inv(player)
        elif cmd in exits:
            move(player, cmd)
        elif " " in cmd.strip():
            # Handle multiple word commands
            words = cmd.split()
            if words[0] == "g" or words[0] == "get":
                get(player, words[1])
            elif words[0] == "d" or words[0] == "drop":
                drop(player, words[1])
            else:
                print("Do what?")
        else:
            print("You can't do that.")


        # if cmd is "look" or cmd is "l":
        #     print(player.location)
        # elif cmd is "quit" or cmd is "q":
        #     print("Goodbye!")
        #     exit
        # exit


if __name__ == '__main__':
    main()