def CountFunction(Sub_String, Main_String, isOverlappingAllowed):
    if not isinstance(Sub_String, str) or not isinstance(Main_String, str):
        return 'TypeError: must be str, not int'

    count = 0
    length_Substring = len(Sub_String)
    length_MainString = len(Main_String)
    
    if isOverlappingAllowed:
        for i in range(length_MainString):
            if Main_String[i:i+length_Substring] == Sub_String:
                count += 1
    else:
        start = 0
        while start < length_MainString:
            pos = Main_String.find(Sub_String, start)
            if pos == -1:
                break
            count += 1
            start = pos + length_Substring

    return count

print(CountFunction('gg', 'sgggggs', True))     #when overlapping is allowed	
print(CountFunction('gg', 'sgggggs', False))   #When Overlappping not allowed
print(CountFunction(5, 'sgggggs', True))      #wrong data 
