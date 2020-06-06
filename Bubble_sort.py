from cube import Run
def bubble():
	run = Run()
	list = run.display()
	length = len(list)

	for i in range(length):
	    for j in range(length-i-1):
	        if list[j] > list[j+1]:
	        	run.remove(list[j],j)
	        	run.remove(list[j+1],j+1)
	        	temp = list[j]
	        	list[j] = list[j+1]
	        	list[j+1] = temp
	        	run.add( list[j],j)
	        	run.add(list[j+1],j+1)
