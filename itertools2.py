

def count(start, step=1):
	while 1:
		yield start
		start+=step

def cycle(p):
	t=[x for x in p] #In case p is a generator
	while 1:
		for x in t:
			yield x

def repeat(elem, n=None):
	if n:
		while n>0:
			yield elem
			n-=1
		return
	else:
		while 1:
			yield elem

def chain(*its):
	# for it in its:
	# 	for elem in it:
	# 		yield elem
	return (elem for it in its for elem in it)