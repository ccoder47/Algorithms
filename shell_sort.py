def shell_sort(arr):
    """
    A generalization of insertion sort with gap sequences.
    Time: O(n^(3/2)) average, Space: O(1)
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


if __name__ == "__main__":
    data = [23, 12, 1, 8, 34, 54, 2, 3]
    print("Unsorted:", data)
    shell_sort(data)
    print("Sorted:  ", data)
