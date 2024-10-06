class Computer:
	def __init__(self, cpu, ram):
		self.cpu=cpu
		self.ram=ram
	def config(self):
		print("config is :",self.cpu,self.ram)
		
		
obj= Computer('i7',512)
obj.config()
