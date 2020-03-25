import math
from time import time

def decompose(n):
    # your code
    for i in range(n):
    	i**2+ decompose(i)
    return None

def sum_squares(n):
	sum_val = 0
	for i in range(n):
		sum_val+=i**2
	return sum_val


def check_squares(n):
	for i in range(n-1,0,-1):
		if n**2 - i**2<=sum_squares(n):
			check_squares(n**2 - i**2)
		elif n**2-i**2==sum_squares(n):
			return 1
		else:
			return 0

		

if __name__ == '__main__':
	t1 = time()
	print(check_squares(5))
	t2 = time()
	print(t2-t1)
	# print(decompose(17))
	# print(decompose(13))
              
    
     