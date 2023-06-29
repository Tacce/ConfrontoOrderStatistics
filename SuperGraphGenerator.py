from GraphTestGenerator import GraphTestGenerator
import matplotlib.pyplot as plt


insertTypeArray = [' Sequential Insert ', ' Random Insert ']


class SuperGraphGenerator:
    def __init__(self, inputDim, accuracy):
        self.n = inputDim
        self.p = accuracy
        self.graphMatrix = []

    def executeTest(self):
        for i in range(3):
            dsRow = []
            for j in range(2):
                g = GraphTestGenerator(i, self.n, j, self.p)
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
            self.__RangeTableAux(data, title, i)
        title = 'OS Rank'
        for i in range(2):
            data = [self.graphMatrix[0][i].yOSRrange,
                    self.graphMatrix[1][i].yOSRrange,
                    self.graphMatrix[2][i].yOSRrange]
            self.__RangeTableAux(data, title, i)

    def plotSingleGraphs(self):
        [[self.graphMatrix[i][j].plotGraphs() for i in range(3)] for j in range(2)]

    def plotSuperGraphInsertType(self):
        for j in range(2):
            title = 'OS Select' + insertTypeArray[j] + str(self.n)
            for i in range(3):
                tmp = self.graphMatrix[i][j]
                plt.plot(tmp.x, tmp.yOSS, label=tmp.structName)
            plt.title(title)
            plt.legend()
            fig = plt.gcf()
            plt.show()
            fig.savefig(title)

        for j in range(2):
            title = 'OS Rank' + insertTypeArray[j] + str(self.n)
            for i in range(3):
                tmp = self.graphMatrix[i][j]
                plt.plot(tmp.x, tmp.yOSR, label=tmp.structName)
            plt.title(title)
            plt.legend()
            fig = plt.gcf()
            plt.show()
            fig.savefig(title)

    def __RangeTableAux(self, data, title, i):
        cell_text = [[f'{x:.3e}' for x in row] for row in data]
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=cell_text, rowLabels=['Linked List', 'ABR', 'ARN'],
                 colLabels=['Fascia Bassa', 'Fascia Media', 'Fascia Alta'], loc='center')
        title += insertTypeArray[i] + str(self.n) + ' Table'
        fig = plt.gcf()
        plt.title(title)
        plt.show()
        fig.savefig(title)
