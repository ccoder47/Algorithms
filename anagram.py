from collections import Counter

def is_anagram(s1, s2):
    """
    Checks if s1 and s2 are anagrams (case-insensitive, ignoring spaces).
    O(n) time, O(n) space.
    """
    clean = lambda s: Counter(c.lower() for c in s if c.isalnum())
    return clean(s1) == clean(s2)

if __name__ == "__main__":
    pairs = [("Listen", "Silent"), ("Hello", "Olelh"), ("Test", "Taste")]
    for a, b in pairs:
        print(f"{a!r} vs {b!r} →", is_anagram(a, b))
