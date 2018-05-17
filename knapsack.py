import Queue

Q = Queue.PriorityQueue()

# class reprenting node in the tree
class Node:
    def __init__(self):
        pass

    'initial value of child node'
    def __init__(self, matrix, parent):
        self.matrix = matrix
        self.parent = parent
        if parent is None:
            self.moves = 0
        else:
            self.moves = parent.moves + 1
        
        '''Calculating 0's position in the specified matrix'''
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == 0:
                    self.x = i
                    self.y = j
    
        self.cost = None    
        
    'Distance between node to destination node'
    def CalculateCost(self, final):
        cost = self.moves
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != final[i][j]:
                    cost += 1
        self.cost = cost
        return cost


# start here
#initial = [list(map(int, raw_input().split(" "))) for i in range(3)]
f#inal = [list(map(int, raw_input().split(" "))) for i in range(3)]
initial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
final = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
obj = Node(initial, None)
obj.CalculateCost(final)