from ARN import ARN
from ABR import ABR
from GraphTestGenerator import GraphTestGenerator
from Lists import LinkedOrderedList
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

insertTypeArray = [' Sequential Insert', ' Random Insert']


def RangeTableAux(data, title, i):
    cell_text = [[f'{x:.3e}' for x in row] for row in data]
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=cell_text, rowLabels=['Linked List', 'ABR', 'ARN'],
             colLabels=['Fascia Bassa', 'Fascia Media', 'Fascia Alta'], loc='center')
    title += insertTypeArray[i]
    plt.title(title)
    plt.show()


class SuperGraphGenerator:
    def __init__(self, inputDim):
        self.n = inputDim
        self.graphMatrix = []

    def executeTest(self):
        for i in range(3):
            dsRow = []
            for j in range(2):
                g = GraphTestGenerator(i, self.n, j, 50)
                g.insertValues()
                dsRow.append(g)
            self.graphMatrix.append(dsRow)

    def plotRangeTable(self):
        [[self.graphMatrix[i][j].rangeTableCalc() for i in range(3)] for j in range(2)]
        title = 'OS Select'
        for i in range(2):
            data = [self.graphMatrix[0][i].yOSSrange,
                    self.graphMatrix[1][i].yOSSrange,
                    self.graphMatrix[2][i].yOSSrange]
            RangeTableAux(data, title, i)
        title = 'OS Rank'
        for i in range(2):
            data = [self.graphMatrix[0][i].yOSRrange,
                    self.graphMatrix[1][i].yOSRrange,
                    self.graphMatrix[2][i].yOSRrange]
            RangeTableAux(data, title, i)

    def plotSingleGraph(self):
        [[self.graphMatrix[i][j].plotGraphs() for i in range(3)] for j in range(2)]

    def plotSuperGraphInsertType(self):
        for j in range(2):
            title = 'OS Select' + insertTypeArray[j]
            for i in range(3):
                tmp = self.graphMatrix[i][j]
                plt.plot(tmp.x, tmp.yOSS, label=tmp.structName)
            plt.title(title)
            plt.legend()
            plt.show()

        for j in range(2):
            title = 'OS Rank' + insertTypeArray[j]
            for i in range(3):
                tmp = self.graphMatrix[i][j]
                plt.plot(tmp.x, tmp.yOSR, label=tmp.structName)
            plt.title(title)
            plt.legend()
            plt.show()


