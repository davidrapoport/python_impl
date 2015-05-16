from itertools2 import *

def chain_test():
	assert list(chain(range(3),range(5))) == [0,1,2,0,1,2,3,4]
