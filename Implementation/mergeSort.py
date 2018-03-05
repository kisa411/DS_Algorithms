# your code goes here
def mergeSort(n):
	length = len(n)
 
	if length == 1 or length == 0:
		return n
 
	halfPt = length//2
 
	a = mergeSort(n[:halfPt])
	b = mergeSort(n[halfPt:])
 
	return merge(a,b)
 
def merge(a,b):
	print (a, b)
	i=j=k=0
	c=[]
	
	
	while(i<len(a) and j<len(b)):
		if a[i] <= b[j]:
			c.append(a[i])
			i=i+1
			k=k+1
		else:
			c.append(b[j])
			j=j+1
			k=k+1
	
	
	if i<len(a):
		c += a[i:]
 
	if j<len(b):
		c += b[j:]

	return c
 
alist = [54,26,93]
print (mergeSort(alist))
 # your code goes here