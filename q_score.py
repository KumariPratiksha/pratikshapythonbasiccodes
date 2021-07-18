A=input("Enter the quality characters: ")
quality=0
for i in A:
	if i=='!':
		quality+=33
	elif i=='"':
		quality+=34
	elif i=='#':
		quality+=35
	elif i=='$':
		quality+=36
	elif i=='%':
		quality+=37
	elif i=='&':
		quality+=38
	elif i=="'":
		quality+=39
	elif i=='(':
			quality+=40
	elif i==')':
			quality+=41
	elif i=='*':
		quality+=42
	elif i =='0':
		quality+=48
	elif i =='1':
		quality+=49
	elif i =='2':
		quality+= 50
	elif i =='3':
		quality+= 51
	elif i =='4':
		quality+= 52
	elif i=='5' :
		quality+=53
	elif i=='6' :
		quality+=54
	elif i=='7' :
		quality+=55
	elif i=='8' :
		quality+=56
	elif i=='9' :
		quality+=57
	elif i==":":
		quality+=58
	elif i==";":
		quality+=59
	elif i=="<":
		quality+=60
	elif i=="=":
		quality+=61
	elif i==">":
		quality+=62
	elif i =='?':
		quality+=63
	elif i =='@':
		quality+=64
	elif i =='A':
		quality+=65
	elif i =='B':
		quality+=66
	elif i =='C':
		quality+=67
	elif i=='D':
		quality+=68
	elif i=='E':
		quality+=69
	elif i=='F':
		quality+=70
	elif i=='G':
		quality+=71
	elif i=='H':
		quality+=72
	elif i=='I':
		quality+=73
	elif i=='J':
		quality+=74
	elif i=='K':
		quality+=75
print (quality)