# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, location, inv=[]):
        self.name = name
        self.location = location
        self.inventory = inv

    def move(self, location):
        self.location = location

    def __repr__(self):
        output = self.name + " " + self.location.name + "\n"
        if len(self.inventory) > 0:
            for i in self.inventory:
                output += i.name + "\n"

    def items(self):
        output = ""
        for i in self.inventory:
            output += i.name + "\n"
        return output

    def item_in_inv(self, item_name):
        for i in self.inventory:
            if item_name in i.name:
                return i
        return None
