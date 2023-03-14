from ARN import ARN
from ABR import ABR
from Lists import LinkedOrderedList
import matplotlib.pyplot as plt
import numpy as np
import time
import random


class GraphicGenerator:
    def __init__(self, structType, structMaxSize, insertType, pointsNumber):
        if structType == 0:
            self.struct = LinkedOrderedList()
        elif structType == 1:
            self.struct = ABR()
        else:
            self.struct = ARN()
        self.structType = structType
        self.structMaxSize = structMaxSize
        self.interval = int(self.structMaxSize / pointsNumber)
        self.insertType = insertType
        self.nodeArray = [None] * self.structMaxSize
        self.x = np.arange(0, structMaxSize + 1, self.interval)
        self.x[0] = 1
        self.yOSS = np.zeros(pointsNumber + 1)
        self.yOSR = np.zeros(pointsNumber + 1)

    def insertValues(self):
        if self.insertType == 0:  # Sequential
            insertArray = np.arange(1, self.structMaxSize + 1)
        else:  # self.insertType == 1:  # Random
            insertArray = random.sample(range(1, self.structMaxSize + 1), self.structMaxSize)
        for i in range(self.structMaxSize):
            self.nodeArray[i] = self.struct.insertNewValue(insertArray[i])
            if i == 0:
                self.yOSS[int((i + 1) / self.interval)] = self.OSSTimeCheck()
                self.yOSR[int((i + 1) / self.interval)] = self.OSRTimeCheck()
            elif (i + 1) % self.interval == 0:
                self.yOSS[int((i + 1) / self.interval)] = self.OSSTimeCheck() + self.yOSS[int(i / self.interval)]
                self.yOSR[int((i + 1) / self.interval)] = self.OSRTimeCheck() + self.yOSR[int(i / self.interval)]
        self.plotGraph(0)
        self.plotGraph(1)

    def OSSTimeCheck(self):
        tmp = np.zeros(self.struct.size)
        for i in range(self.struct.size):
            start = time.perf_counter()
            self.struct.OS_Select(i + 1)
            end = time.perf_counter()
            tmp[i] = (end - start) / self.struct.size
        return np.mean(tmp)

    def OSRTimeCheck(self):
        tmp = np.zeros(self.struct.size)
        for i in range(self.struct.size):
            start = time.perf_counter()
            self.struct.OS_Rank(self.nodeArray[i])
            end = time.perf_counter()
            tmp[i] = (end - start) / self.struct.size
        return np.mean(tmp)

    def plotGraph(self, graphType):
        if graphType == 0:
            title = 'OS Select '
            y = self.yOSS
        else:
            title = 'OS Rank '
            y = self.yOSR

        if self.structType == 0:
            title += 'Linked List '
        elif self.structType == 1:
            title += 'ABR '
        else:
            title += 'RN '

        if self.insertType == 0:
            title += 'Sequential Order '
        elif self.insertType == 1:
            title += 'Random Insert'

        plt.plot(self.x, y)
        plt.title(title)
        plt.show()

    def rangeTableDisplay(self):
        n = int(self.structMaxSize / 3)
        print('MEDIE OSS FASCE VALORI')
        print(np.mean(self.yOSS[:n]))
        print(np.mean(self.yOSS[n:2 * n]))
        print(np.mean(self.yOSS[2 * n:]))
        return np.mean(self.yOSS)
