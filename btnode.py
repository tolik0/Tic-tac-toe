class Node(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, data):
        self.data = data
        self.res = None
        self.children = []