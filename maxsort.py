def maxsort(E):
    n = len(E)
    for i in range(n - 1, 0, -1):  # Iterate through indexes
        max_int = 0  # first element starts off as max
        for j in range(1, i + 1):  # Find max in the unsorted section of array
            if E[j] > E[max_int]:
                max_int = j
        # interchange max with the element in the last position in the unsorted section
        E[max_int], E[i] = E[i], E[max_int]

#Tests
tests = [
    [77, 7, 74, 47, 17],
    [10, 20, 30, 40, 50],  # sorted test case
    [57, 71, 27, 73, 774],
    [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],  # reverse sorted test case
    [32, 41, 44, 771, 705, 809, 42, 63, 576, 33]
]

for test in tests:
    print(f"Unsorted: {test}")
    maxsort(test)
    print(f"Sorted:   {test}\n")
