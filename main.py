from SuperGraphGenerator import SuperGraphGenerator

if __name__ == '__main__':
    while True:
        x = int(input("Inserisci dimensione test:"))
        if x == 0:
            break
        while True:
            y = int(input("Inserisci numero di punti:"))
            if x % y == 0:
                break
        test = SuperGraphGenerator(x, y)
        test.executeTest()
        test.plotRangeTable()
        test.plotSuperGraphInsertType()
        test.plotSingleGraphs()
