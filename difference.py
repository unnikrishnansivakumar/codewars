def twos_difference(lst): 
    list_ret = []
    for i in lst:
        for j in lst:
            if j-i == 2:
                list_ret.append((i,j))
    return sorted(list_ret,key = lambda x: x[1])
                