class DefaultList(list):
	def __init__(self,lst_v,default_val):
		self.list = lst_v
		self.default_val = default_val
	def __getitem__(self,index):
		if index<=len(list(self.lst_v))-1:
			return list(self.lst_v)[index]
		else:
			return self.default_val

if __name__ == '__main__':
	a = DefaultList([1,2,3,4],'Def')
	print(a[1])

