from Trees import ABR
from Trees import ABRNode
from Lists import LinkedOrderedList
import matplotlib.pyplot as plt
import numpy as np
import time

if __name__ == '__main__':
    Mylist = ABR()
    Mylist.insertNewValue(51)
    Mylist.insertNewValue(14)
    Mylist.insertNewValue(12)
    Mylist.insertNewValue(64)
    Mylist.insertNewValue(23)
    Mylist.insertNewValue(3)
    Mylist.displayTree()
    x = Mylist.OS_Select(1)
    if x is not None:
        print(x.key)
    print(Mylist.OS_Rank(12))
