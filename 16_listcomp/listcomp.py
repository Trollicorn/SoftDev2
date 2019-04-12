from functools import reduce
from operator import mul

def min(pw):
	"""
	return if password has
	a mix of uppwer and lowercase letters
	and at least 1 number
	"""
	lis = [2 if c.isdigit() else 3 if c.islower() else 5 if c.isupper() else 7 for c in pw]
	pro = reduce(mul,lis)
	a= float(pro)/(2*3*5)
	b= pro//(2*3*5)*1.0
	return a==b

print ("abc is " + str(min("abc")) + " and should be False") #False
print ("AbC is " + str(min("AbC")) + " and should be False") #False
print ("b12 is " + str(min("b12")) + " and should be False") #False
print ("rpBc4 is " + str(min("rpBc4")) + " and should be True") #True

def strong(pw):
	"""
	return if password is strong
	"""
	lis = [2 if c.isdigit() else 3 if c.islower() else 5 if c.isupper() else 7 for c in pw]
	pro = reduce(mul,lis)
	strn = 0
	if pro % 2 == 0:
		strn += 1
	if pro % 4 == 0:
		strn += 1
	if pro % 3 == 0:
		strn += 1
	if pro % 9 == 0:
		strn += 1
	if pro % 5 == 0:
		strn += 1
	if pro % 25 == 0:
		strn += 1
	if pro % 7 == 0:
		strn += 1
	if pro % 49 == 0:
		strn += 1
	if pro % (2*3*5*7) == 0:
		strn += 1
	if strn == 9:
		strn += 1
	return strn

print("hello is " + str(strong("hello")) + " and should be 2") #2
print("hello12 is " + str(strong("hello12")) + " and should be 4") #4
print("HelLo0,3! is " + str(strong("HelLo0,3!")) + " and should be 10") #10
