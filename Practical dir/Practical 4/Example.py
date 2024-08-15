Capital_Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Small_Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ChangeStyle(Text, Style):
    if Style in ['s', 'S']:
        return Small_Case(Text)
    return Text 
    elif Style in ['c','C']:
    	return  Capital_Case(Text)
			
def Small_Case(Text):
    Styled_String = ''
    for i in range(len(Text)):
        if Text[i] in Capital_Alphabets:
            for j in range(len(Capital_Alphabets)):
                if Text[i] == Capital_Alphabets[j]:
                    Styled_String += Small_Alphabets[j]
                    break
        else:
            Styled_String += Text[i]  
    return Styled_String
    
def Capital_Case(Text):
	Styled_String = ''
	for i in Text:
		for j in range(len(Capital_Alphabets)):
                if Text[i] == Small_Alphabets[j]:
                    Styled_String += Capital_Alphabets[j]
                    break
        else:
            Styled_String += Text[i]  
    return Styled_String

print(ChangeStyle("SGGS", "S"))
print(ChangeStyle("Sggs", "S"))

