def fibonacci(n):
    """
    Computes the n-th Fibonacci number iteratively.
    Time: O(n), Space: O(1)
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    for i in range(10):
        print(f"Fibonacci({i}) =", fibonacci(i))
