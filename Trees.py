class ABR:
    osCounter = 0
    found = False
    rankedNode = None

    def __init__(self):
        self.root = None
        self.size = 0

    def insertNewValue(self, newValue):
        newNode = ABRNode(newValue)
        y = None
        x = self.root
        while x is not None:
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
        return newNode

    def display(self):
        self.preorderTreeWalk(self.root)
        print('\n', end='')

    def preorderTreeWalk(self, x):
        if x is not None:
            print(x.key, end='(')
            self.preorderTreeWalk(x.left)
            print(end=',')
            self.preorderTreeWalk(x.right)
            print(end=')')
        else:
            print(end='-')

    def inorderTreeWalkSelect(self, x, i):
        if x is not None:  # and not self.found:
            self.inorderTreeWalkSelect(x.left, i)
            if self.osCounter is i and not self.found:
                self.found = True
                self.rankedNode = x
            else:
                self.osCounter += 1
                self.inorderTreeWalkSelect(x.right, i)

    def inorderTreeWalkRank(self, x, node):
        if x is not None:  # and not self.found:
            self.inorderTreeWalkRank(x.left, node)
            if x.key is node.key and not self.found:
                self.found = True
            elif not self.found:
                self.osCounter += 1
                self.inorderTreeWalkRank(x.right, node)

    def OS_Select(self, i):
        self.osCounter = 1
        self.inorderTreeWalkSelect(self.root, i)
        self.osCounter = 0
        self.found = False
        x = self.rankedNode
        self.rankedNode = None
        return x

    def OS_Rank(self, node):
        self.osCounter = 1
        self.inorderTreeWalkRank(self.root, node)
        i = self.osCounter
        self.osCounter = 0
        self.found = False
        if i > self.size:
            i = 0
        return i


class ABRNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
