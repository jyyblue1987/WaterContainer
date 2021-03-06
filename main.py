from graph import Graph
from queue2050 import Queue
import math
import unittest

def bfs(g,start):
    result = []
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
        result.append(currentVert.getId())

    return result
        

def bfs_find(g,start, goal):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        id = currentVert.id
        if id[0] == goal or id[1] == goal:  # reach to goal state
            return id

        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

    return None

def path2root(y):
    x = y    
    result = []
    while (x.getPred()):
        # print(x.getId())
        result.append(x.getId())
        x = x.getPred()
    # print(x.getId())
    result.append(x.getId())

    return result

def build_graph(a, b):
    g = Graph()

    vertex_list = []
    for i in range(0, a + 1):
        for j in range(0, b + 1):
            vertex_list.append((i, j))

    for u in vertex_list:
        # fiil A
        if u[0] < a:
            g.addEdge(u, (a, u[1]))

        # fill B
        if u[1] < b:
            g.addEdge(u, (u[0], b))

        # A => B
        if u[0] > 0 and u[1] < b:
            amount = min(b - u[1], u[0])
            g.addEdge(u, (u[0] - amount, u[1] + amount))

        # B => A
        if u[0] < a and u[1] > 0:
            amount = min(a - u[0], u[1])
            g.addEdge(u, (u[0] + amount, u[1] - amount))

    return g

def findSolution(a, b, goal_amount):    
    c = math.gcd(a, b)
    remain = goal_amount % c
    if goal_amount % c != 0:
        return None

    # a) building the graph as needed
    g = build_graph(a, b)
    
    # b) performing BFS
    id = bfs_find(g, g.getVertex((0, 0)), goal_amount)
    if id == None:
        return []

    # c) navigating the result of BFS to return the solution path as Python list of tuples
    result = path2root(g.getVertex(id))

    return result

# return a list of tuples that are possible states that be reached from the current state (denoted by curr_state )
def getEligibleStates(a, b, curr_state):
    g = build_graph(a, b)

    result = bfs(g, g.getVertex(curr_state))
    
    return result


def main():
    result = findSolution(5, 8, 2)
    print(result)

    result = getEligibleStates(3, 4, (3, 3))
    print(result)

class adjGraphTests(unittest.TestCase):
    def setUp(self):
        pass

    def testFindSolution(self):
        result = findSolution(3, 4, 2)
        self.assertEqual(result, [(2, 4), (3, 3), (0, 3), (3, 0), (0, 0)])

    def testEligibleStates(self):
        result = getEligibleStates(3, 4, (3, 3))
        self.assertEqual(result, [(3, 3), (3, 4), (2, 4)])

if __name__ == "__main__":
    main()
    unittest.main()