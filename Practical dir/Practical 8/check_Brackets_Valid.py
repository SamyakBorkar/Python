valid_Symbol = ("<", ">", "{", "}", "[", "]", "(", ")")

def check_validity(text):
    for char in text:
        if char not in valid_Symbol:
            return "Invalid Text: Contains characters that are not valid symbols"
    
    stack = []
    mapping_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    
    for bracket in text:
        if bracket in mapping_dict:
            stack.append(bracket)
        else:
            if stack and mapping_dict[stack[-1]] == bracket:
                stack.pop()
            else:
                return "Invalid Text: Mismatched closing bracket"
    
    if len(stack) == 0:
        return "Valid Text"
    else:
        return "Invalid Text: Unmatched opening bracket(s)"

text = "(<{}>)"
print(check_validity(text))

