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

  def show_exits(self):
    exits = ""
    if self.n_to is not None:
      exits += "n "
    if self.s_to is not None:
      exits += "s "
    if self.w_to is not None:
      exits += "w "
    if self.e_to is not None:
      exits += "e "
    return exits
