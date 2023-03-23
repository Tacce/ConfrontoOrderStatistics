from ARN import ARN
from ABR import ABR
from Lists import LinkedOrderedList
import matplotlib.pyplot as plt
import numpy as np
import time
import random


class GraphTestGenerator:

    def __init__(self, structType, structMaxSize, insertType, pointsNumber):
        if structType == 0:
            self.struct = LinkedOrderedList()
            self.structName = 'Linked List'
        elif structType == 1:
            self.struct = ABR()
            self.structName = 'ABR'
        else:
            self.struct = ARN()
            self.structName = 'ARN'
        self.structType = structType
        self.structMaxSize = structMaxSize
        self.interval = int(self.structMaxSize / pointsNumber)
        self.insertType = insertType
        self.nodeArray = [None] * self.structMaxSize
        self.x = np.arange(0, structMaxSize + 1, self.interval)
        self.x[0] = 1
        self.yOSS = np.zeros(pointsNumber + 1)
        self.yOSR = np.zeros(pointsNumber + 1)
        self.yOSSrange = np.zeros(3)
        self.yOSRrange = np.zeros(3)

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

    def plotGraphs(self):
        self.plotOSGraph(0)
        self.plotOSGraph(1)

    def OSSTimeCheck(self, rangeTable=0):
        tmp = np.zeros(self.struct.size)
        for i in range(self.struct.size):
            start = time.perf_counter()
            self.struct.OS_Select(i + 1)
            end = time.perf_counter()
            tmp[i] = (end - start) / self.struct.size
        if not rangeTable:
            return np.mean(tmp)
        else:
            n = int(self.structMaxSize / 3)
            self.yOSSrange[0] = np.mean(tmp[:n])
            self.yOSSrange[1] = np.mean(tmp[n: 2 * n])
            self.yOSSrange[2] = np.mean(tmp[2 * n:])

    def OSRTimeCheck(self, rangeTable=0):
        tmp = np.zeros(self.struct.size)
        for i in range(self.struct.size):
            start = time.perf_counter()
            self.struct.OS_Rank(self.nodeArray[i])
            end = time.perf_counter()
            tmp[i] = (end - start) / self.struct.size
        if not rangeTable:
            return np.mean(tmp)
        else:
            n = int(self.structMaxSize / 3)
            self.yOSRrange[0] = (np.mean(tmp[:n]))
            self.yOSRrange[1] = (np.mean(tmp[n:2 * n]))
            self.yOSRrange[2] = (np.mean(tmp[2 * n:]))

    def plotOSGraph(self, graphType):
        if graphType == 0:
            title = 'OS Select '
            y = self.yOSS
        else:
            title = 'OS Rank '
            y = self.yOSR
        title += self.structName
        if self.insertType == 0:
            title += ' Sequential Order '
        elif self.insertType == 1:
            title += ' Random Insert '
        title += str(self.structMaxSize)
        plt.plot(self.x, y)
        plt.title(title)
        plt.show()
        # plt.savefig(title)

    def rangeTableCalc(self):
        self.OSSTimeCheck(1)
        self.OSRTimeCheck(1)

