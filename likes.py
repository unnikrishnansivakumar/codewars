def likes(names):
    #your code here
    if len(names)==0:
        return 'no one likes this'
    elif len(names)==1:
        return names[0]+' likes this'
    elif len(names)==2:
        return '%s and %s like this'%(names[0],names[1])
    elif len(names)==3:
        return  '%s and %s like this'%(', '.join(names[:-1]),names[-1])
    else:
    	return  '%s and %d others like this'%(', '.join(names[:2]),len(names)-2)


if __name__ == '__main__':
	# print(likes(['Gayatri','Unni','Asha','Sivan','Priya','Manu','Meera']))
	# print(likes(['Gayatri','Unni','Asha','Sivan']))
	# print(likes(['Gayatri','Unni','Asha']))
	# print(likes(['Gayatri','Unni']))
	# print(likes(['Gayatri']))
	print([(i,j)for i,j in enumerate('Gayatri')])
        