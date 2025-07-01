def selection_sort(arr):
    """
    Selects the minimum element from the unsorted portion and swaps it into place.
    Time: O(n^2), Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Unsorted:", data)
    selection_sort(data)
    print("Sorted:  ", data)
