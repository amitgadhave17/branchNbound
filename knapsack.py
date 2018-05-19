'''
Following is solution for 8 puzzle problem using branch and bound technique.
Author - Amit Gadhave
Date : 19 may 2018

'''
import time
import Queue

Q = Queue.PriorityQueue()

#following artay is been used for calculating the child node for given node(Means calculating left, right, top, down swap positio in the game)
xd = [-1, 0, 1, 0]
yd = [0, 1, 0, -1]

# class reprenting node in the tree
class Node:
    def __init__(self):
        pass

    def __cmp__(self, other):
        return cmp(self.totalCost, other.totalCost)

    'initial value of root node'
    @staticmethod
    def CreateRoot(matrix):
        node = Node()
        node.matrix = matrix
        node.parent = None
        node.moves = 0
        '''Calculating 0's position in the specified matrix'''
        for i in range(3):
            for j in range(3):
                if node.matrix[i][j] == 0:
                    node.x = i
                    node.y = j
    
        node.cost = None
        node.totalCost = None    
        return node

    'This is contructor for new child node' 
    @staticmethod 
    def CreateChild(parent, i ):
        node = Node()
        node.matrix = parent.matrix
        node.parent = parent
        node.moves = parent.moves + 1
        node.x = parent.x + xd[i]
        node.y = parent.y + yd[i]
        node.matrix = [[parent.matrix[i][j] for j in range(3)] for i in range(3)]
        node.matrix[node.x][node.y] = parent.matrix[parent.x][parent.y]
        node.matrix[parent.x][parent.y] = parent.matrix[node.x][node.y]
        return node

    'Distance between node to destination node'
    def CalculateCost(self, final):
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != final[i][j]:
                    cost += 1
        self.cost = cost
        self.totalCost = self.moves + self.cost
        return cost

    def __str__(self):
        return "\n".join([" ".join(list(map(str, self.matrix[i]))) for i in range(3)])

def IsValid(i, j):
    if(i < 0 or j < 0 or i > 2 or j > 2):
        return False
    return True

def PrintPath(node):
    if(node is None):
        print("Printing Optimal path to Destination")
        return
    PrintPath(node.parent)
    print(str(node))
    print("---------------")
 
def FindRoute(final):
    while(not Q.empty()):
        cur_node = Q.get()
        print(cur_node)
        print("---------------")
        if cur_node.cost == 0:
            PrintPath(cur_node)
            return cur_node
        for i in range(4):
            if(IsValid(cur_node.x + xd[i], cur_node.y + yd[i])):
                child_node = Node.CreateChild(cur_node, i)
                child_node.CalculateCost(final)
                Q.put(child_node)


# start here
#initial = [list(map(int, raw_input().split(" "))) for i in range(3)]
#final = [list(map(int, raw_input().splt(" ")) for i in range(3)]
initial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
final = [[2, 3, 6], [1, 0, 5], [4, 7, 8]]
obj = Node.CreateRoot(initial)
obj.CalculateCost(final)
Q.put(obj)
FindRoute(final)
