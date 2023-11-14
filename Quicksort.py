def QuickSort(arr):
    if(len(arr) <= 1):
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)
numbers = [50, 10, 20, 100, 100, 90, 80, 40, 120, 30, 200, 0]
print(QuickSort(numbers))
