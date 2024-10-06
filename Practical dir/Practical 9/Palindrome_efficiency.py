import time

def is_palindrome_method1(n):
    s = str(n)
    return s == s[::-1]

def is_palindrome_method2(n):
    s = str(n)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def count_palindromes_divisible_by_3(numbers, method):
    count = 0
    for num in numbers:
        if method(num) and num % 3 == 0:
            count += 1
    return count

def efficiency_test(numbers, iterations=100):
    start1 = time.time()
    for _ in range(iterations):
        count_palindromes_divisible_by_3(numbers, is_palindrome_method1)
    time1 = time.time() - start1

    start2 = time.time()
    for _ in range(iterations):
        count_palindromes_divisible_by_3(numbers, is_palindrome_method2)
    time2 = time.time() - start2

    return time1, time2

numbers = [121, 12321, 111, 303, 202, 33, 1234321, 45654, 101, 909, 33] * 10
iterations = 100
time_method1, time_method2 = efficiency_test(numbers, iterations)

print("Time taken by Method 1 (String Slicing):", time_method1)
print("Time taken by Method 2 (Two-pointer):", time_method2)

if time_method1 < time_method2:
    print("Method 1 is faster.")
else:
    print("Method 2 is faster.")
