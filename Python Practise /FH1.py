def read_char(f):
	l=f.read()
	d=dict()
	for i in l:
		d[i]=d.get(i,0)+1
	return d
	
fi=open('dummy','r')
print(read_char(fi))