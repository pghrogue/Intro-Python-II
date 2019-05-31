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


def main():
    '''Entry point for the game and command loop.'''
    
    name = input("Brave adventurer! What is your name? ")
    player = Player(name, room['outside'])

    print(f"Welcome to your adventure, {player.name}!\n\n")
    commands = ("l", "q")

    look(player)

    while True:
        cmd = input("What would you do? ")
        exits = player.location.get_exits()

        # Command loop.
        if cmd == "look" or cmd == "l":
            look(player)
        elif cmd == "quit" or cmd == "q":
            quit_game()
        elif cmd in exits:
            move(player, cmd)
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