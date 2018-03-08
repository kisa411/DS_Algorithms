class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class OrderedList():
	def __init__(self):
		self.head = None
		self.size = 0
		
	def add(self, elem):
		newNode = Node(elem)
		curr = self.head
		print(curr)
		while (curr!=None and curr.getValue() < elem):
			print('go through loop')
			curr = curr.getNext()
			
		if (curr == None): #insert new node at end
			curr.setNext(newNode)
			
		else:
			newNode.setNext(curr.getNext())
			curr.setNext(newNode)
		
		self.size+=1
		
		
newList = OrderedList()
print (newList)

newList.add(5)
'''
newList.add(6)
newList.add(3)
print (newList)
'''