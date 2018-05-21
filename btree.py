from btnode import Node


class Tree():
    """An link-based binary tree implementation."""

    def __init__(self):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __iter__(self):
        """Supports a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                lyst.append(node.data)
                for nod in node.children:
                    recurse(nod)
        recurse(self._root)
        return iter(lyst)

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        for i in self:
            if item == i.data:
                return True
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None

    def add(self, item, child):
        """Adds item to the tree."""
        child = Node(child)
        item.children.append(child)

    def set_root(self, item):
        self._root = Node(item)

    def height(self):
        '''
        Return the height of tree
        :return: int
        '''

        def height1(p):
            """Return the height of the subtree rooted at Position p."""
            if p.children == []:
                return 0
            else:
                return 1 + max(height1(c) for c in p.children)

        return height1(self._root)


tree = Tree()
tree._root = Node("a")
for i in range(3):
    tree.add(tree._root, i)
for j in tree._root.children:
    for i in range(3):
        tree.add(j, i)
child = tree._root.children[0]
