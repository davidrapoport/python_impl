import itertools2 as it
import itertools as it_orig
import unittest

class TestItertools(unittest.TestCase):

	def test_chain(self):
		chain_list = list(it.chain(range(3),range(5)))
		self.assertEqual([0,1,2,0,1,2,3,4],chain_list)

	def test_count(self):
		l = []
		gen = it.count(0,2)
		for i in gen:
			l.append(i)
			if i>=10:
				break
		self.assertEqual(len(l),6)
		self.assertEqual(l,[0,2,4,6,8,10])

	def test_cycle(self):
		gen = it.cycle(range(5))
		cnt = 0
		l = []
		for i in gen:
			if cnt>=10:
				break
			l.append(i)
			cnt +=1
		self.assertEqual(len(l),10)
		s = set([0,1,2,3,4])
		self.assertEqual(s|set(l),s&set(l))

	def test_repeate(self):
		l = list(it.repeat('a',12))
		k = list(it_orig.repeat('a',12))
		self.assertEqual(l,k)

	def test_groupby(self):
		self.assertEqual(it.groupby([1,1,1,1,2,2,2,3,3,1]), [(key,list(group)) for (key,group) in it_orig.groupby([1,1,1,1,2,2,2,3,3,1])])
		l = lambda x: x%2
		self.assertEqual(it.groupby([1,2,3,5,7,9,4,4,4,8,7],l),[(key,list(group)) for (key,group) in it_orig.groupby([1,2,3,5,7,9,4,4,4,8,7],l)])

if __name__=='__main__':
	unittest.main()