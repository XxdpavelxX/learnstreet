



def string_rot13(str):
	total = []
	
	for char in str:
		a = ord(char)+13   #new numerical value that shall later be converted to number
		if ord(char)>109:
			a = 97 + (a - 123) #109+13+1=123 which is first ord value for lowerercase letter that goes above alphabet
			total.append(chr(a))
		elif 77<ord(char)<84:
			a = 65 + (a - 91)   #77+13+1= 91 which is first ord value for uppercase letters that goes above alphabet
			total.append(chr(a))
		elif 65>ord(char) or 90<ord(char)<97 or ord(char)>122:  #for chars that are not alphabetic
			pass   
		else:
			total.append(chr(a))   #all regular letters that do not go below or above alphabet value
	ans = ''.join(total)
    return ans
