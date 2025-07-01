def linear_search(arr, target):
    """
    Scans each element until it finds the target.
    Returns the index or -1 if not found. Time: O(n), Space: O(1)
    """
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


if __name__ == "__main__":
    data = [10, 23, 45, 70, 11, 15]
    target = 70
    idx = linear_search(data, target)
    print(f"Target {target} found at index {idx}" if idx != -1 else "Target not found")
