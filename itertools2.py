import copy

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
	return (elem for it in its for elem in it)

def compress(data, selectors):
	for d,s in zip(data,selectors):
		if s:
			yield d

def dropwhile(pred, seq):
	flag = False
	for i in seq:
		flag = flag or (not pred(i))
		if flag:
			yield i

def groupby(iterable, keyfunc=None):
	keys = []
	groups = []
	if keyfunc is None or not hasattr(keyfunc,'__call__'):
		keyfunc = lambda x: x
	if not len(iterable):
		return ([],[])
	key = keyfunc(iterable[0])
	l = []
	l.append(iterable[0])
	keys.append(key)
	for i in iterable[1:]:
		if key != keyfunc(i):
			key =keyfunc(i)
			groups.append(l)
			l = []
			l.append(i)
			keys.append(key)
		else:
			l.append(i)
	if l:
		groups.append(l)
	return zip(keys,groups)

def ifilter(seq, pred=None):
	if pred is None:
		pred = lambda x: x
	return (s for s in seq if pred(s))

def ifilterfalse(seq, pred=None):
	if pred is None:
		pred = lambda x: x
	return (s for s in seq if not pred(s))

def islice(seq,start=0,stop=None,step=1):
	while 1:
		if stop and start>stop:
			return
		try:
			l = seq[start]
			start += step
			yield l
		except:
			return
def imap(func, *args):
	for values in zip(args):
		if func:
			yield func(*values)
		else:
			yield tuple(*values) #is the call to tuple necessary?

def starmap(func, seq):
	return (func(*i) for i in seq)

def tee(it, n):
	pass #Dont get it right now

def takewhile(pred, seq):
	if pred is None:
		pred = bool
	if not len(seq):
		return
	i = 0
	while i<len(seq) and pred(seq[i]):
		yield seq[i]
		i += 1

def izip(*its):
	iterables = map(iter, its)
	while 1:
		try:
			yield tuple(map(next,iterables))
		except:
			return

def izip_longest(*its, **kwargs):
	fillvalue = kwargs.get("fillvalue")
	lists=map(list,its)
	longest = reduce(lambda acc,x: max(acc,len(x)),lists, 0)
	iterables = map(iter,lists)
	for i in range(longest):
		yield tuple([next(x,fillvalue) for x in iterables])
		#Alternate version using any() to see if any of them aint fillvalue? instead of getting longest?

def product(*args, **kwargs):
	def inner(*seqs, **kwargs):
		repeat = kwargs.get("repeat")
		if repeat:
			seqs = seqs*repeat
		if not len(seqs):
			yield []
		elif len(seqs) == 1:
			for i in seqs[0]:
				yield [i]
		else:
			temp = list(inner(*seqs[1:])) # Has to be a list otherwise it gets exhausted
			for i in seqs[0]:
				for lst in temp:
					l = [i]+copy.deepcopy(lst)
					yield l

	for i in inner(*args,**kwargs):
		yield tuple(i)


