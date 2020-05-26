import random
"""
Array sorting algorithms
"""

#PythonDefault implemented 
def defaultsort(array):
    array.sort()
    return array

#Pivot implemented 
unsorted = [random.randint(1,100) for _ in range(20)]
def pivotsort(array):
    if len(array) < 1:
        return array
    else:
        pivot = array[0]
        left = []
        right = []
        for num in range(1, len(array)):
            if array[num] < pivot:
                left.append(array[num])
            else:
                right.append(array[num]) 
    return pivotsort(left) + [pivot] + pivotsort(right)

#Bubble sort implemented 
def bubblesort(array):
    donesorting = False
    for i in range(len(array)):
        while not donesorting:
            donesorting = True
            if array[i] > array[i +1]:
                donesorting = False
                temp = array[i]
                array[i] = array[i + 1]
                array[i+1] = temp
    return array 

"""
Array Searching algorithms
"""
def bisectionrootsearch(value):
    def indelta(fixedvalue, variablevalue, delta=0.005):
        if (variablevalue > fixedvalue - delta) and (variablevalue < fixedvalue + delta):
            return True 
        else:
            return False

    upper = value 
    lower = 0 
    while True:
        pivot = (upper + lower) /2 
        if pivot**2 > value and not indelta(pivot**2, value): 
            upper = pivot 
        elif pivot **2  < value and not indelta(pivot**2 , value):
            lower = pivot 
        else:
            return pivot



#bogosort
def issorted(sortlist):
    previous = sortlist[0]
    for i in range(1, len(sortlist)):
        if  not sortlist[i] >= previous:
            return False 
        previous = sortlist[i]
    return True 

def bogosort(sortlist):
    operations = 0 
    while not issorted(sortlist):
        random.shuffle(sortlist)
        operations += 1 
    return sortlist , operations


print(pivotsort([random.randint(1,10) for i in range(20)]))