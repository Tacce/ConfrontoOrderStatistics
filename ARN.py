from ABR import ABR
from ABR import ABRNode

BLACK = True
RED = False


class ARN(ABR):
    def __init__(self):
        ABR.__init__(self)

    def insertNewValue(self, newValue):
        newNode = ARNNode(newValue)
        y = None
        x = self.root
        while x is not None:
            x.size += 1
            y = x
            if newNode.key < x.key:
                x = x.left
            else:
                x = x.right
        newNode.p = y
        if y is None:
            self.root = newNode
        elif newNode.key < y.key:
            y.left = newNode
        else:
            y.right = newNode
        self.size += 1
        self.insertFixup(newNode)
        return newNode

    def insertFixup(self, newNode):
        while newNode.p is not None and newNode.p.color == RED:
            if newNode.p == newNode.p.p.left:
                y = newNode.p.p.right
                if y is not None and y.color == RED:
                    newNode.p.color = BLACK
                    y.color = BLACK
                    newNode.p.p.color = RED
                    newNode = newNode.p.p
                else:
                    if newNode == newNode.p.right:
                        newNode = newNode.p
                        self.left_rotate(newNode)
                    newNode.p.color = BLACK
                    newNode.p.p.color = RED
                    self.right_rotate(newNode.p.p)
            else:
                y = newNode.p.p.left
                if y is not None and y.color == RED:
                    newNode.p.color = BLACK
                    y.color = BLACK
                    newNode.p.p.color = RED
                    newNode = newNode.p.p
                else:
                    if newNode == newNode.p.left:
                        newNode = newNode.p
                        self.right_rotate(newNode)
                    newNode.p.color = BLACK
                    newNode.p.p.color = RED
                    self.left_rotate(newNode.p.p)
        self.root.color = BLACK

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        y.size = 1 + (y.left.size if y.left is not None else 0) + (y.right.size if y.right is not None else 0)
        x.size = 1 + (x.left.size if x.left is not None else 0) + (x.right.size if x.right is not None else 0)

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        x.size = 1 + (x.left.size if x.left is not None else 0) + (x.right.size if x.right is not None else 0)
        y.size = 1 + (y.left.size if y.left is not None else 0) + (y.right.size if y.right is not None else 0)

    def OS_Select(self, i):
        x = self.root
        found = False
        while not found and x is not None:
            j = (x.left.size if x.left is not None else 0) + 1
            if j is i:
                found = True
            elif i < j:
                x = x.left
            else:
                x = x.right
                i = i-j

        return x

    def OS_Rank(self, x):
        i = (x.left.size if x.left is not None else 0) + 1
        y = x
        while y is not self.root:
            if y is y.p.right:
                i += (y.p.left.size if y.p.left is not None else 0) + 1
            y = y.p
        return i


class ARNNode(ABRNode):
    def __init__(self, key):
        ABRNode.__init__(self, key)
        self.size = 1
        self.color = RED

    def printNode(self):
        if self.color is RED:
            print('R', end='')
        else:
            print('B', end='')
        print(self.key, end='(')
