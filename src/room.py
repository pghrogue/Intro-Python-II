import textwrap
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    output = f'"{self.name}"\n'
    output += self.description + "\n"
    return textwrap.fill(output)

room = Room("test","a test room")
print(room)