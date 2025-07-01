def gcd(a, b):
    """
    Computes the greatest common divisor of two integers via the Euclidean algorithm.
    Time: O(log min(a, b)), Space: O(1)
    """
    while b:
        a, b = b, a % b
    return abs(a)


if __name__ == "__main__":
    x, y = 48, 18
    print(f"GCD({x}, {y}) =", gcd(x, y))
