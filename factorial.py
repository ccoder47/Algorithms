def factorial(n):
    """
    Computes n! using an iterative loop.
    Time: O(n), Space: O(1)
    """
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


if __name__ == "__main__":
    for i in range(6):
        print(f"{i}! =", factorial(i))
