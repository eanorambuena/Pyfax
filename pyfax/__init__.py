class Cache(list):
	def __init__(self):
		super().__init__()
	def found(self, x):
		for c in self:
			if x == c[0]:
				return c[1]
		return None
	def storage(self, x, value):
		self.append([x, value])

cache = Cache()
cache.storage(0, 1)
cache.storage(1, 1)

def f(x):
	result = cache.found(x)
	if result != None:
		return result
	else:
		result = x * f(x-1)
		cache.storage(x, result)
		return result

r1 = f(5)

class Function():
	def __init__(self, base_cases = []):

		self.cache = Cache()

		for case in base_cases:
			self.cache.storage(case)
	

class f(Function):
	def __init__(self):
		super().__init__([[0,1], [1,1]])
	def function(self, x):
		result = self.cache.found(x)
		if result != None:
			return result
		else:
			result = x * f(x-1)
			self.cache.storage(x, result)
			return result
	def precompute(self, x):
		for i in range(0, x + 50, 50):
			self.function(i)
	def eval(self, x):
		self.precompute(x)
		return self.function(x)

#r2 = f.eval(5)
print(r1)
