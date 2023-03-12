from ARN import ARN
from ABR import ABR
from Lists import LinkedOrderedList
import matplotlib.pyplot as plt
import numpy as np
import time
import random


class GraphicGenerator:
    def __init__(self, structType, structSize, testType, insertType):
        if structType == 0:
            self.struct = LinkedOrderedList()
        elif structType == 1:
            self.struct = ABR()
        else:
            self.struct = ARN()
        self.structSize = structSize
        self.testType = testType
        self.insertType = insertType
        self.x = np.arange(1, structSize + 1)  # TODO spostare alcuni attributi in appositi metodi
        self.yOSS = np.zeros(structSize)

    def insertValues(self):
        if self.insertType == 0:  # Sequenziale
            for i in range(self.structSize):
                self.struct.insertNewValue(i + 1)
        elif self.insertType == 1:  # Randomico
            randomArray = random.sample(range(1, self.structSize + 1), self.structSize)
            for i in range(self.structSize):
                self.struct.insertNewValue(randomArray[i])
        elif self.insertType == 2:
            for i in range(self.structSize, 0, -1):
                self.struct.insertNewValue(i)

    def drawOSSGraph(self):
        for i in range(self.structSize):
            start = time.perf_counter()
            self.struct.OS_Select(i + 1)
            end = time.perf_counter()
            self.yOSS[i] = (end - start)/self.structSize
        plt.plot(self.x, self.yOSS)
        plt.show()
        n = int(self.structSize/3)
        print(np.mean(self.yOSS[:n]))
        print(np.mean(self.yOSS[n:2*n]))
        print(np.mean(self.yOSS[2*n:]))
