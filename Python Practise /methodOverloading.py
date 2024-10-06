class A:
	def __init__(self,v1,v2):
		self.v1=v1
		self.v2=v2
	def sum(self,*a):
		return sum(a)

a=A(1,2)
print(a.sum(6,5,4))
print(a.sum(6,5))

