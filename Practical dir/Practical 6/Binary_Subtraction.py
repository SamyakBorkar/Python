def binary_Subtraction(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    result = ''
    borrow = 0

    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])

        bit2 = bit2 + borrow

        if bit1 < bit2:
            borrow = 1
            result = str(bit1 + 2 - bit2) + result
        else:
            borrow = 0
            result = str(bit1 - bit2) + result

    result = result.lstrip('0')

    if result == '':
        return '0'

    return result

bin1 = "1101"   # 13 in decimal
bin2 = "101"    # 5 in decimal
print(binary_Subtraction(bin1, bin2))  # Output should be "1000" (8 in decimal)
