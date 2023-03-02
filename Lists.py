class OrderedList:
    def __init__(self):
        self.list = []
        self.size = 0

    def displayList(self):
        for i in range(self.size):
            print(self.list[i], end=' ')

    def insertNewValue(self, value):
        i = 0
        while i < self.size and value > self.list[i]:
            i += 1
        self.list.insert(i, value)
        self.size += 1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedOrderedList:
    def __init__(self):
        self.head = None

    def displayList(self):
        if self.head is None:
            print('Lista Vuota')
        else:
            tmpNode = self.head
            while tmpNode is not None:
                print(tmpNode.value, end=' ')
                tmpNode = tmpNode.next
            print('\n', end='')

    def insertNewValue(self, newValue):
        newNode = Node(newValue)
        if self.head is None:
            self.head = newNode
        elif newValue <= self.head.value:
            newNode.next = self.head
            self.head = newNode
        else:
            tmpNode = self.head
            while tmpNode.next is not None and newValue > tmpNode.next.value:
                tmpNode = tmpNode.next
            newNode.next = tmpNode.next
            tmpNode.next = newNode

    def OS_Select(self, i):
        j = 1
        tmpNode = self.head
        while tmpNode is not None and j is not i:
            j += 1
            tmpNode = tmpNode.next
        return tmpNode

    def OS_Rank(self, key):
        tmpNode = self.head
        i = 1
        while tmpNode is not None and tmpNode.value is not key:
            tmpNode = tmpNode.next
            i += 1
        if tmpNode is None:
            i = '{ph} non appartiene alla lista'.format(ph=key)
        return i


