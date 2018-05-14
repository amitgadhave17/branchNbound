import Queue

Q = Queue.PriorityQueue()



initial = [map(int, input().split(" ")) for i in range(3)]
final = [map(int, input().split(" ")) for i in range(3)]
Q.put(initial)

