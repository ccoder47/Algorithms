def bubble_sort(arr):
    """
    Repeatedly steps through the list, swapping adjacent out-of-order elements.
    Time: O(n^2), Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted:", data)
    bubble_sort(data)
    print("Sorted:  ", data)
