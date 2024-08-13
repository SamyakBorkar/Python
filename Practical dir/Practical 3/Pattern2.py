def print_pattern(n):
    for i in range(2 * n + 1):
        for j in range(2 * n + 1):
            if i <= n:
                if j == n - i or j == n + i:
                    print("+ ", end="")
                else:
                    print("   ", end="")
            else:
                if i == 2 * n and j == n:  
                    print("- ", end="")
                elif j == i - n or j == 3 * n - i:  
                    print("+ ", end="")
                else:
                    print("   ", end="")
        print()


print_pattern(3)

