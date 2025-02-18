import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # Convert list into a heap
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

# Example usage
arr = [5, 3, 8, 6, 2, 7, 4, 1]
print(heap_sort(arr))
