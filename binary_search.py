def binary_search(arr, target):
    """
    On a sorted array, repeatedly halves the search interval to find a target.
    Returns the index or -1 if not found. Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    target = 7
    idx = binary_search(data, target)
    print(f"Target {target} found at index {idx}" if idx != -1 else "Target not found")
