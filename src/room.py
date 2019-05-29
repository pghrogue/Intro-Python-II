import textwrap
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.w_to = None
    self.e_to = None

  def __str__(self):
    output = f'"{self.name}"\n'
    output += textwrap.fill(self.description, 70, initial_indent='    ') + "\n"
    return output


test = Room("test", "Just another test room with a bunch of descriptive words and stuff. I wonder what else we can add here, I'd like to make it pretty long. I guess this is good enough.")
print(test)

test.n_to = Room("another test", "Here we have another test room, but this one doesn't have as much detail to it.")
print(test.n_to)