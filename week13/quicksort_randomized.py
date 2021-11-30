import random

def quicksort(arr, start , stop):
    if(start < stop):

        pivotindex = partitionrand(arr,
                             start, stop)

        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)

def partitionrand(arr , start, stop):

    randpivot = random.randrange(start, stop)

    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
 

def partition(arr,start,stop):
    pivot = start 
    i = start + 1

    for j in range(start + 1, stop + 1):

        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
 
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print(array)


    # Using random pivoting we improve the expected or 
    # average time complexity to O (N log N). 
    # The Worst-Case complexity is still O ( N^2 ).