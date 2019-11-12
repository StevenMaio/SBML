class Node:

    def __init__(self, parent=None):
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent
