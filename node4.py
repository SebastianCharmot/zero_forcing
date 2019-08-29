from itertools import combinations

class Node:

    def __init__(self, infected, id):
        self.neighbors = []
        self.infected = infected
        self.id = id
        uninfected_nodes.append(self)
    def addNeighbor(self, neighborNode):
        self.neighbors.append(neighborNode)

uninfected_nodes = []
polynomial = []
xpower = 0

def generatecombinations():
    from itertools import combinations
    combs = []
    possibilities = []
    r = 1
    for i in range(len(uninfected_nodes)):
        possibilities.append(i)
    while r < len(uninfected_nodes) + 1:
        for combination in combinations(possibilities, r):
            combs.append(list(combination))
        r += 1
    print(combs)
    for i in range(len(combs)):
        # print(combs[i])
        infect(combs[i]) #pass into infect the values from combinations that it wants to infect
        for node in uninfected_nodes:
            node.infected = False #set state back to everything uninfected

def infect(victims):
    operating_nodes = uninfected_nodes
    xpower = len(victims)
    for victim in victims:
        operating_nodes[victim].infected = True
    # for node in operating_nodes:
    #     print(node.id, node.infected)
    print(xpower)
    print(victims)
    forcing(operating_nodes)

    #pass on list of Node objects with certain nodes infected to function forcing
    return True

def forcing(graph):
    for node in graph:
        count = 0
        if node.infected == True:
            if len(node.neighbors) == 0:
                pass
            for neighbor in node.neighbors:
                if neighbor.infected == False:
                    count += 1
            if count == 1:
                for neighbor in node.neighbors:
                    neighbor.infected = True
                    # forcing(graph)
    for node in graph:
        print(node.id, node.infected)
    print("-----------")

    #run logic of forcing  
    #force until no change then goes to function forced
    return True

def forced():
    #check whether each node is forced or not
    #check xpower to see which index of polynomial to add to
    return True

if __name__ == '__main__':
    Node1 = Node(False, "1")
    Node2 = Node(True, "2")
    Node3 = Node(False, "3")
    # Node4 = Node(False, "3")
    # Node5 = Node(False, "3")

    Node1.addNeighbor(Node2)
    Node2.addNeighbor(Node1)
    Node2.addNeighbor(Node3)
    # Node3.addNeighbor(Node4)
    # Node4.addNeighbor(Node5)

    # test = [Node1, Node2, Node3]
    # forcing(test)

    generatecombinations()
    # infect(0)


