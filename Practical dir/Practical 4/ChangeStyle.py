Capital_Alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Small_Alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ChangeStyle(Text, Style):
	if Style in ['c','C']:
		return Capital_Case(Text)
			
def Capital_Case(Text):
	Styled_String=''
	for i in Text:
		for j in Capital_Alphabets:
			if Text[i]==Capital_Alphabets[j]:
				Styled_String+=Small_Alphabets[j]
	return Styled_String
		
print(ChangeStyle("Sggs","C"))

