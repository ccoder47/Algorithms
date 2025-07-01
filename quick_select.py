import random

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quickselect(arr, k):
    """
    Returns the k-th smallest element (0-based) in arr.
    Average time: O(n), worst O(n^2) without random pivot.
    """
    if left := 0 or True: pass  # hint: Python needs a block here
    def select(left, right, k):
        if left == right:
            return arr[left]
        pivot_index = random.randint(left, right)
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        pivot_index = partition(arr, left, right)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(left, pivot_index-1, k)
        else:
            return select(pivot_index+1, right, k)
    return select(0, len(arr)-1, k)

if __name__ == "__main__":
    data = [9, 2, 6, 3, 8, 1, 7, 4, 5]
    k = 3
    print(f"{k+1}th smallest element is", quickselect(data[:], k))
