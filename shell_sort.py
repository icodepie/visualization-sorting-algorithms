from cube import Run
def shell_sort():
	run = Run()
	arr = run.display()
	sublistcount = len(arr) // 2
	
	while sublistcount > 0:
		for start in range(sublistcount):
			gap_insertion_sort(arr,start,sublistcount,run)
		#print(sublistcount)
		#print(arr)
		sublistcount = sublistcount // 2

	return arr

	
def gap_insertion_sort(arr, start, gap,run):
	for i in range(start+gap, len(arr),gap):

		currentvalue = arr[i]
		position = i

		while position >= gap and arr[position-gap] > currentvalue:
			run.remove(arr[position-gap],position-gap)
			run.remove(arr[position],position)
			arr[position] = arr[position-gap]
			run.add( arr[position],position)
			position = position-gap
		arr[position] = currentvalue
		run.add( arr[position],position)




# shell_sort()