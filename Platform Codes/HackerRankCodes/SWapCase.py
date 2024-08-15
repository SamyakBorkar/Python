def swap_case(s):
    t=str.swapcase(s)
    return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)