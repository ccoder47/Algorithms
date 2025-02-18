def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choosing middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  # For duplicates
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [5, 3, 8, 6, 2, 7, 4, 1]
print(quick_sort(arr))
