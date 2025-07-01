def insertion_sort(arr):
    """
    Builds the sorted array one item at a time by inserting elements into the correct position.
    Time: O(n^2) (fast on nearly-sorted), Space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Unsorted:", data)
    insertion_sort(data)
    print("Sorted:  ", data)
