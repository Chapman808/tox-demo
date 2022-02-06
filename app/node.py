class Node:
    def __init__ (self, val, next):
        self.val = val
        self.next = next
    def __str__ (self):
        return "{" + str(self.val) + ": " + str(self.next) + "}"
    def __eq__ (self, other):
        if type(other) != Node: return False
        return str(self) == str(other)