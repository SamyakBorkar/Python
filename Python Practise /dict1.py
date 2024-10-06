def Give_dictCount(l):
	data=dict()
	for first, second in l:
		data.setdefault(first, []).append(second)
	return data
		
		
		
pairs = [('fruit', 'apple'), ('fruit', 'banana'), ('veggie', 'carrot')]
print(Give_dictCount(pairs))
