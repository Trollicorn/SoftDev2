def repeat(word):
	def ok(x):
		return word * x
	return ok
print('\nTEST REPEAT\n')
r1 = repeat('hello')
r2 = repeat('goodbye')
print(r1(2))
print(r2(2))
print(repeat('cool')(3))

def make_counter():
	x = 0
	def count():
		nonlocal x
		x += 1
		return x
	def see():
		nonlocal x
		return x
	return [count,see]
print('\nTEST COUNTER\n')
print('COUNTER 0')
ctrl = make_counter()
print(ctrl[0]())
print(ctrl[0]())
print(ctrl[0]())
print('ACCESS 0')
print(ctrl[1]())
print('COUNTER 1')
ctrl2 = make_counter()
print(ctrl2[0]())
print(ctrl2[0]())
print('COUNTER 0')
print(ctrl[0]())
print('COUNTER 1')
print(ctrl2[0]())
print('ACCESS 0')
print(ctrl[1]())
print('ACCESS 1')
print(ctrl2[1]())
