class A:
	def __init__(self):
		print("Init A")
	def f1(self):
		print("Feature 1")
	def f2(self):
		print("Feature 2")
		
class B:
	def __init__(self):
		super().__init__()
		print("Init B")
	def f3(self):
		print("Feature 3")
	def f4(self):
		print("Feature 4")
		
class C(B,A):
	def __init__(self):
		super().__init__()
		super().__init__()
		print("INIT C")
	def f6(self):
		print("Feature 5")
	def f5(self):
		print("Feature 6")
		
#b=B()
c=C()
