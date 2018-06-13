import string

class Token:
	def __init__(self,v):
		self.value=v
	def __repr__(self):
		return self.value

class Connective(Token):
	def __init__(self,v,a,b):
		self.value=v
		self.a=a
		self.b=b
	def __repr__(self):
		return str(self.a)+str(self.b)+self.value
class Negation(Token):
	def __init__(self,a):
		self.a=a
	def __repr__(self):
		return str(self.a)+"N"

def find_end_of_first(txt):
	stack=[[txt[0],0]]
	j=0
	for i in range(1,len(txt)):
		if txt[i] in string.ascii_lowercase:
			stack[-1][1]+=1
		elif txt[i] in "KACEN":
			stack.append([txt[i],0])
		while (stack[-1][0] in "KACE" and stack[-1][1]==2) or (stack[-1][0]=="N" and stack[-1][1]==1):
			stack.pop()
			stack[-1][1]+=1
		if stack[0][1]==1 or len(stack)==0:
			j=i+1
			break
	return j
			
def tokenize(txt):
	if txt[0] in "KACE":
		return(Connective(txt[0], tokenize(txt[1:find_end_of_first(txt)]),tokenize(txt[find_end_of_first(txt):])))
	elif txt[0] =="N":
		return Negation(tokenize(txt[1:]))
	elif txt[0] in string.ascii_lowercase:
		return Token(txt[0])

print(str(tokenize('KNap')))
print(str(tokenize('NEKApNqNCqpr')))
