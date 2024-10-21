def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point to divide the array into two halves
        mid = len(arr) // 2
       
        # Dividing the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]
       
        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)
       
        i = j = k = 0
       
        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
       
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
       
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
