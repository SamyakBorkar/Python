Capital_Alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Small_Alphabets = 'abcdefghijklmnopqrstuvwxyz'

def Capital_Case(text):
    result = ''
    for char in text:
        if char in Small_Alphabets:
            index = Small_Alphabets.index(char)
            result += Capital_Alphabets[index]
        else:
            result += char
    return result

def Small_Case(text):
    result = ''
    for char in text:
        if char in Capital_Alphabets:
            index = Capital_Alphabets.index(char)
            result += Small_Alphabets[index]
        else:
            result += char
    return result

def Zigzag(text):
    result = ''
    if text and text[0] in Capital_Alphabets:
        toggle = True
    else:
        toggle = False

    for char in text:
        if char in Small_Alphabets:
            if toggle:
                result += Capital_Alphabets[Small_Alphabets.index(char)]
            else:
                result += char
            toggle = not toggle
        elif char in Capital_Alphabets:
            if toggle:
                result += char
            else:
                result += Small_Alphabets[Capital_Alphabets.index(char)]
            toggle = not toggle
        else:
            result += char

    return result

def Reverse(text):
    result = ''
    for char in text:
        if char in Small_Alphabets:
            result += Capital_Alphabets[Small_Alphabets.index(char)]
        elif char in Capital_Alphabets:
            result += Small_Alphabets[Capital_Alphabets.index(char)]
        else:
            result += char
    return result

def ChangeCase(text, style):
    if style == 'c' or style == 'C':
        return Capital_Case(text)
    elif style == 's' or style == 'S':
        return Small_Case(text)
    elif style == 'z' or style == 'Z':
        return Zigzag(text)
    elif style == 'r' or style == 'R':
        return Reverse(text)
    else:
        return text


print(ChangeCase('Hello World!', 'C'))  # Output: 'HELLO WORLD!'
print(ChangeCase('Hello World!', 'S'))  # Output: 'hello world!'
print(ChangeCase('Hello World!', 'Z'))  # Output: 'HeLlO wOrLd!'
print(ChangeCase('hello World!', 'Z'))  # Output: 'hElLo wOrLd!'
print(ChangeCase('Hello World!', 'R'))  # Output: 'hELLO wORLD!'
