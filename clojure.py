import math
def comp(array1, array2):
    if array1==None or array2==None:
        return 900
    elif len(array1)==len(array2):
        return False not in [i*i==j for i,j in zip(sorted(array1,key = lambda x:abs(x)),sorted(array2,key = lambda x:abs(x)))]
    else:
        for i in array2:
            if math.sqrt(i) not in array1:
                return False
            else:
                array1.remove(math.sqrt(i))
        return True
    

a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a1, a2))