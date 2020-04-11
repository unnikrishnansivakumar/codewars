def next_num(n):
	numbers= list(str(n))
	for i in range(1,len(numbers)+1):
		if int(''.join(numbers[:i]))%(i)==0 and int(numbers[i-1])!=0:
			pass
		else:
			diff = int(''.join(numbers[:i]))%i
			numbers = list(str(int(''.join(numbers[:i]))+(i-diff))+''.join(numbers[i:]))
	return int(''.join(numbers))
			
	
	
if __name__ == '__main__':
	print(next_num(100))