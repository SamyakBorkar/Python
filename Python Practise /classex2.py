class example:
	school="Oasis"
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		
	#instance Method
	def Avg(self):
		return (self.a+self.b+self.c)/3
	
	#class Method
	@classmethod
	def get_schoolname(cls):
		return cls.school
		
	@staticmethod
	def info():
		print("static method function")
	
obj=example(5,6,3)
print(obj.Avg())
print(obj.get_schoolname())
example.info()
print(type(example))
