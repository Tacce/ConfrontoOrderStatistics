from GraphicGenerator import GraphicGenerator
from ARN import ARN

if __name__ == '__main__':
    Mygraph = GraphicGenerator(2, 100, 0, 1)
    Mygraph.insertValues()
    Mygraph.drawOSSGraph()
