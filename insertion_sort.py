from cube import Run

def sort():
	run = Run()
	array = run.display()
	for i in range(1,len(array)):
		currentvalue = array[i]
		position = i
		while position > 0 and array[position-1] > currentvalue:
			run.remove(array[position],position)
			run.remove(array[position-1],position-1)
			array[position] = array[position - 1]
			run.add( array[position],position)
			position = position - 1
			array[position] = currentvalue
			run.add( array[position],position)


