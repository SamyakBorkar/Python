class outer:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.inn=self.inner()
		print("in outer")
		
	def __init__(self):
		print("default")
	def show(self):
		pass
		
		
	class inner:
		def __init__(self):
			print("in inner class")
			
#obj=outer('sam','20')
obj=outer()
