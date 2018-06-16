#This is program which calculate maximum profit of knapsack for the given input
#Author -	Amit Gadhave
#Date 	- 	28/01/2018

try:
    import Queue as Q  
except ImportError:

    import queue as Q
    
#size of knapsack
ksize= 10
q = Q.PriorityQueue()

#item profit per unit stored sorted in this array.
decprofit=[]
weight=[5.0,3.0,2,1]
profit=[15.0,12.0,10,6] 

#total number of items.
noi=len(weight)

#class object which store item at level of different object
#This item include level,profit till level and weight till level and maximum bound which for knapsack 
class Item(object):
	def __init__(self, ilevel, iweight, iprofit, ibound):
		self.level=ilevel
		self.weight=iweight
		self.profit=iprofit
		self.bound=ibound
	def __cmp__(self, other):
		return cmp(other.bound,self.bound)
        
def swap(array,m,n):
	 temp=array[m]
	 array[m]=array[n]
	 array[n]=temp

def sort():
	l=len(weight)
	for i in range(l-1):
		for j in range(l-1):
			if(decprofit[j]<decprofit[j+1]):
				swap(decprofit,j,j+1)
				swap(weight,j,j+1)
				swap(profit,j,j+1)
 
def bound(level, iweight,iprofit):
	while  level < noi and (iweight+weight[level]) <= ksize :
		iweight = iweight+weight[level]
		iprofit= iprofit+profit[level]
		level=level+1;
	if(level<noi):
		iprofit=iprofit+(ksize-iweight)*decprofit[level]
	return iprofit
		
def knapsack():
	while not q.empty():
		a=q.get()
		if(a.level == noi):
			return a.profit 
		if(a.weight+weight[a.level]) <= ksize:
			q.put(Item(a.level+1, a.weight+weight[a.level], a.profit+profit[a.level], a.bound))
		q.put(Item(a.level+1, a.weight, a.profit, bound(a.level+1, a.weight, a.profit)))

if __name__=="__main__":
	decprofit=[(profit[i]/weight[i]) for i in range(len(weight))]
	sort()

	a=Item(0,0,0,bound(0,0,0))
	q.put(a) 
	a=knapsack()
	print a 
