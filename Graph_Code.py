# Graph and Basic Graph Algorithms


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


class Vertex:
    def __init__(self, ver):
        self.id = ver
        self.connectedto = {}
        self.color = 'white'
        self.pred = None

    def addNeighbor(self, t, cost=0):
        self.connectedto[t] = cost

    def getConnections(self):
        return self.connectedto.keys()

    def getColor(self):
        return self.color

    def setColor(self, col):
        self.color = col

    def setPred(self, pr):
        self.pred = pr

    def getPred(self):
        return self.pred


class Graph:
    def __init__(self):
        self.vertlist = {}

    def addVertex(self, item):

        self.vertlist[item] = Vertex(item)
        return Vertex(item)

    def addEdge(self, f, t, cost=0):

        if f not in self.vertlist:
            nf = self.addVertex(f)

        if t not in self.vertlist:
            nt = self.addVertex(t)

        self.vertlist[f].addNeighbor(self.vertlist[t], cost)

    def getVertex(self, v):
        if v in self.vertlist:
            return self.vertlist[v]
        else:
            return None


g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'E')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'E')


# Breadth First Search
def bfs_graph(start):
    myq = Queue()
    myq.enqueue(start)

    start.setColor('yellow')

    while not myq.isEmpty():
        nv = myq.dequeue()

        print nv.id

        for item in nv.getConnections():
            if item.getColor() == 'white':
                item.setColor('yellow')
                item.setPred(nv)
                myq.enqueue(item)


print bfs_graph(g.getVertex('A'))


def shortest_path(start):
    while start is not None:
        print start.getPred().id
        start = start.getPred()


print shortest_path(g.getVertex('E'))

# Before running DFS code, comment out BFS code


# Depth First Search
def dfs_graph(start):
    if start.getColor() == 'yellow':
        return

    start.setColor('yellow')

    print start.id

    for nodes in start.getConnections():
        dfs_graph(nodes)


print dfs_graph(g.getVertex('A'))
