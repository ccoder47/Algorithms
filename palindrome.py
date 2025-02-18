def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is the same forwards and backwards
    return s == s[::-1]

# Test the function
test_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome!")
else:
    print(f"'{test_string}' is not a palindrome.")
