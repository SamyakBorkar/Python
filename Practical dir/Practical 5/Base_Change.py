def base_conversion(text: str, input_base: int, output_base: int) -> str:
    if input_base == 'R':
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        def roman_to_int(roman: str) -> int:
            total, prev_value = 0, 0
            for char in reversed(roman):
                value = roman_map[char]
                if value < prev_value:
                    total -= value
                else:
                    total += value
                prev_value = value
            return total

        num = roman_to_int(text)
    elif 2 <= input_base <= 36:
        def to_int(text: str, base: int) -> int:
            if base == 10:
                return int(text)
            try:
                return int(text, base)
            except ValueError:
                return "Invalid input for base conversion."

        num = to_int(text, input_base)
        if isinstance(num, str):
            return num
    else:
        return "Unsupported input base."

    def int_to_roman(num: int) -> str:
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        roman = ''
        for value, symbol in value_map:
            while num >= value:
                roman += symbol
                num -= value
        return roman

    def from_int(value: int, base: int) -> str:
        if base == 10:
            return str(value)
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if value == 0:
            return "0"
        result = ""
        while value > 0:
            result = digits[value % base] + result
            value //= base
        return result

    if output_base == 'R':
        return int_to_roman(num)
    elif 2 <= output_base <= 36:
        return from_int(num, output_base)
    else:
        return "Unsupported output base."

# Test cases
print(base_conversion("1010", 2, 10))          # Output: "10"
print(base_conversion("10", 10, 2))            # Output: "1010"
print(base_conversion("X", 'R', 10))           # Output: "10"
print(base_conversion("10", 10, 'R'))          # Output: "X"
print(base_conversion("MMXXIV", 'R', 10))      # Output: "2024"
print(base_conversion("2024", 10, 'R'))        # Output: "MMXXIV"
print(base_conversion("12", 10, 'R'))          # Output: "XII"
print(base_conversion("1010", 2, 'R'))         # Output: "X"
