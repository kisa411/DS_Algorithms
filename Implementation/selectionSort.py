
def selectionSort(array):
	lastIndex = len(array)
	for j in range(0, len(array)):
		positionOfMax = 0
		for i in range(0, len(array) - j):
			if (array[i] > array[positionOfMax]):
				positionOfMax = i
		temp = array[positionOfMax]
		array[positionOfMax] = array[len(array)-1-j]
		array[len(array)-1-j] = temp

	
	
A = [3, 25, 4, 22, 11]
print(selectionSort(A))