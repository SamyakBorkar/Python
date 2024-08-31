def Slice(Object, Start=None, Stop=None, Step=1):
    length = len(Object)
    
    if Step == 0:
        return "Step can't be Zero"
    
    if Start is None:
        Start = 0 if Step > 0 else length - 1
    if Stop is None:
        Stop = length if Step > 0 else -1
    
    if Start < 0:
        Start += length
    if Stop < 0:
        Stop += length
    
    if Start < 0:
        Start = 0
    elif Start > length:
        Start = length

    if Stop < 0:
        Stop = 0
    elif Stop > length:
        Stop = length

    if Step > 0 and Start > Stop:
        return ""
    if Step < 0 and Start < Stop:
        return ""

    result = ""
    if Step > 0:
        i = Start
        while i < Stop:
            result += Object[i]
            i += Step
    else:
        i = Start
        while i > Stop:
            result += Object[i]
            i += Step
    
    return result

Object = "Samyak Borkar"
print(Slice(Object, 2))  # Output: "myak Borkar"
print(Slice(Object, 2, 8, 2))  # Output: "my"
print(Slice(Object, -1, -8, -2))  # Output: "rka"
