class student:
	def __init__(self,v1,v2):
		self.v1=v1
		self.v2=v2
	def __add__(self,other):
		m1=self.v1+other.v1
		m2=self.v2+other.v2
		m3=student(m1,m2)
		return m3
		
	def __str__(self):
		return '{} {}'.format(self.v1, self.v2)
		
		
		
s1=student(3,7)
s2=student(6,9)
s3=s1+s2
print(s3.v1)
print("_____")
print(s1.__str__())
print(s2)
print(s3)
