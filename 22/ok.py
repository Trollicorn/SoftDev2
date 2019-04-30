def make_counter():
	x = 0
	def reee():
		nonlocal x
		x += 1
		return x
	return reee

ctrl = make_counter()
print(ctrl())
print(ctrl())
print(ctrl())
ctrl2 = make_counter()
print(ctrl2())
print(ctrl2())
print(ctrl())
print(ctrl2())
