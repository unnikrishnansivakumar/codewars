from collections import Counter,OrderedDict

def more_zeros(s):	
	binary = [i for i in s if check_greater(bin(ord(i))[2:])==1]
	return list(OrderedDict.fromkeys(binary))
	

def check_greater(num):
	if Counter(num)['0']> Counter(num)['1']:
		return 1
	else:
		return -1

if __name__ == '__main__':
	print(more_zeros('abcdeahgdjkl'))