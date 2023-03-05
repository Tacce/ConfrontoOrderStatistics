class ListNode:
    def __init__(self, value):
        self.key = value
        self.next = None


class LinkedOrderedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print('Lista Vuota')
        else:
            tmpNode = self.head
            while tmpNode is not None:
                print(tmpNode.key, end=' ')
                tmpNode = tmpNode.next
            print('\n', end='')

    def insertNewValue(self, newValue):
        newNode = ListNode(newValue)
        if self.head is None:
            self.head = newNode
        elif newValue <= self.head.key:
            newNode.next = self.head
            self.head = newNode
        else:
            tmpNode = self.head
            while tmpNode.next is not None and newValue > tmpNode.next.key:
                tmpNode = tmpNode.next
            newNode.next = tmpNode.next
            tmpNode.next = newNode
        return newNode

    def OS_Select(self, i):
        j = 1
        tmpNode = self.head
        while tmpNode is not None and j is not i:
            j += 1
            tmpNode = tmpNode.next
        return tmpNode

    def OS_Rank(self, node):
        tmpNode = self.head
        i = 1
        while tmpNode is not None and tmpNode.key is not node.key:
            tmpNode = tmpNode.next
            i += 1
        if tmpNode is None:
            i = 0
        return i


