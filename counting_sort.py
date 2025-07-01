def counting_sort(arr):
    """
    Sorts non-negative integers using counting sort.
    Time: O(n + k), Space: O(k), where k = max(arr).
    """
    if not arr:
        return arr
    mx = max(arr)
    count = [0] * (mx + 1)
    for v in arr:
        count[v] += 1
    idx = 0
    for val, freq in enumerate(count):
        for _ in range(freq):
            arr[idx] = val
            idx += 1

if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("Unsorted:", data)
    counting_sort(data)
    print("Sorted:  ", data)
