from ARN import ARN
from ABR import ABR
from Lists import LinkedOrderedList
import matplotlib.pyplot as plt
import numpy as np
import time

if __name__ == '__main__':
    Mylist = ARN()
    n51 = Mylist.insertNewValue(51)
    n14 = Mylist.insertNewValue(14)
    n12 = Mylist.insertNewValue(12)
    n64 = Mylist.insertNewValue(64)
    n23 = Mylist.insertNewValue(23)
    n3 = Mylist.insertNewValue(3)
    Mylist.display()
    x = Mylist.OS_Select(1)
    if x is not None:
        print(x.key)
    print(Mylist.OS_Rank(n64))
