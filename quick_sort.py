
from cube import Run

def quick_sort():
    run = Run()
    arr = run.display()

    quick_sort_help(arr,0,len(arr)-1,run)

def quick_sort_help(arr,first,last,run):
    
    if first<last:
        
        splitpoint = partition(arr, first, last,run)
        
        quick_sort_help(arr,first,splitpoint-1,run)
        quick_sort_help(arr,splitpoint+1,last,run)
        
def partition(arr,first,last,run):
    
    pivotvalue = arr[first]
    
    leftindex = first+1
    rightindex = last
    
    done = False
    while not done:
        
        while leftindex <= rightindex and arr[leftindex] <= pivotvalue:
            leftindex = leftindex + 1
            
        while arr[rightindex] >= pivotvalue and rightindex >= leftindex:
            rightindex = rightindex - 1
            
        if rightindex < leftindex:
            done = True
        else:
            run.remove(arr[leftindex],leftindex)
            run.remove(arr[rightindex],rightindex)
            temp = arr[leftindex]
            arr[leftindex] = arr[rightindex]
            run.add( arr[leftindex],leftindex)
            arr[rightindex] = temp
            run.add( arr[rightindex],rightindex)
    
    run.remove(arr[first],first)
    run.remove(arr[rightindex],rightindex)
    temp = arr[first]
    arr[first] = arr[rightindex]
    run.add( arr[first],first)
    arr[rightindex] = temp
    run.add( arr[rightindex],rightindex)
    return rightindex

