def two_sum(nums, target):
    """
    Returns indices of the two numbers that add up to target.
    O(n) time, O(n) space.
    """
    seen = {}
    for i, v in enumerate(nums):
        needed = target - v
        if needed in seen:
            return [seen[needed], i]
        seen[v] = i
    return []

if __name__ == "__main__":
    data = [2, 7, 11, 15]
    target = 9
    print("Indices:", two_sum(data, target))
