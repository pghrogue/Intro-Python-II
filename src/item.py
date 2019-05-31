# Implement a class to hold item information. This should have name and
# description attributes.

class Item:

  def __init__(self, name, desc):
    self.name = name
    self.desc = desc

  def __str__(self):
    return self.name

  def description(self):
    return self.desc