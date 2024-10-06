from abc import ABC, abstractmethod
class Computer(ABC):
	@abstractmethod
	def process(self):
		pass
class Laptop(Computer):
	def process(self):
		print("Hey this is laptop")
	
	def d(dummy):
		print("meowwww......")	
		
l=Laptop()
l.process()
