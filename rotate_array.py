def rotate_right(arr, k):
    """
    Rotates the array to the right by k steps in-place.
    Time: O(n), Space: O(1).
    """
    n = len(arr)
    k %= n
    arr[:] = arr[-k:] + arr[:-k]

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original:", data)
    rotate_right(data, k)
    print(f"Rotated by {k}:", data)
