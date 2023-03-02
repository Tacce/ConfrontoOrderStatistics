from Lists import OrderedList
from Lists import Node
from Lists import LinkedOrderedList


if __name__ == '__main__':
    Mylist = LinkedOrderedList()
    Mylist.insertNewValue(51)
    Mylist.insertNewValue(14)
    Mylist.insertNewValue(12)
    Mylist.insertNewValue(64)
    Mylist.insertNewValue(23)
    Mylist.insertNewValue(3)
    Mylist.displayList()
    if Mylist.OS_Select(6) is not None:
        print(Mylist.OS_Select(6).value)
    print(Mylist.OS_Rank(3))
