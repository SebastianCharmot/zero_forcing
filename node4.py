from itertools import combinations

class Node:

    def __init__(self, infected, id):
        self.neighbors = []
        self.infected = infected
        self.id = id
        uninfected_nodes.append(self)
        polynomial.append(0)
    def addNeighbor(self, neighborNode):
        self.neighbors.append(neighborNode)
        neighborNode.neighbors.append(self)

uninfected_nodes = []
polynomial = []

def start_forcing():
    generate_combinations()

def generate_combinations():
    from itertools import combinations
    combs = [] #nested list of combinations of node id's
    possibilities = [] #list of node id's
    r = 1
    for i in range(len(uninfected_nodes)):
        possibilities.append(i)
    while r < len(uninfected_nodes) + 1:
        for combination in combinations(possibilities, r):
            combs.append(list(combination))
        r += 1
    for i in range(len(combs)):
        infect(combs[i]) #pass into infect the values from combinations that it wants to infect
        for node in uninfected_nodes:
            node.infected = False #set nodes back to uninfected before infecting new nodes

def infect(victims):
    operating_nodes = uninfected_nodes
    xpower = len(victims)
    for victim in victims:
        operating_nodes[victim].infected = True
    forcing(operating_nodes, xpower) #pass on list of Node objects with inital nodes infected

def forcing(graph, xpower):
    forced = 0 #Keep track of whether or not something was forced when looping through graph
    for node in graph: #Forcing logic
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
                    forced += 1
    if forced >= 1: #If something was forced then we want to do forcing logic again
        forcing(graph, xpower) #Can potentially be used to see how many forces it takes to fully infect a graph
    else: #After going through the entire graph no nodes were forced, so we are done forcing
        check(graph,xpower) #pass nodes into check function 

def check(postforcing, xpower): # determines whether graph was fully forced or not
    unforced = 0
    for node in postforcing:
        if node.infected == False:
            unforced += 1
    if unforced == 0:     #verify all nodes are forced
        polynomial[xpower-1] += 1       #check xpower to see which index of polynomial to add to

if __name__ == '__main__': #Example shown is a graph of 10 nodes connected in a straight line
    Node0 = Node(False, "0")
    Node1 = Node(False, "1")
    Node2 = Node(False, "2")
    Node3 = Node(False, "3")
    Node4 = Node(False, "4")
    Node5 = Node(False, "5")
    Node6 = Node(False, "6")
    Node7 = Node(False, "7")
    Node8 = Node(False, "8")
    Node9 = Node(False, "9")

    Node0.addNeighbor(Node1)
    Node1.addNeighbor(Node2)
    Node2.addNeighbor(Node3)
    Node3.addNeighbor(Node4)
    Node4.addNeighbor(Node5)
    Node5.addNeighbor(Node6)
    Node6.addNeighbor(Node7)
    Node7.addNeighbor(Node8)
    Node8.addNeighbor(Node9)

    start_forcing()
    print(polynomial)

