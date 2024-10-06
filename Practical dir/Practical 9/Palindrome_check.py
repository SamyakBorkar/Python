def count_palindromes_divisible_by_3(numbers):
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]
    
    count = 0
    for num in numbers:
        if is_palindrome(num) and num % 3 == 0:
            count += 1
    return count

# Example Usage
numbers = [121, 12321, 111, 303, 202, 33]
result = count_palindromes_divisible_by_3(numbers)
print("Count:", result)
