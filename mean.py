def mean(town, strng):
    citywise = strng.split('\n')
    string_val = [i.split(":")[1] for i in citywise if i.split(":")[0]==town]
    if len(string_val)>0:
        array_val = {i.split()[0]:i.split()[1] for i in string_val[0].split(",")}
    else:
        array_val = {}
    if array_val != {}:
        return sum([float(i) for i in array_val.values()])/len(array_val.values())
    else:
        return -1.0
    
    
def variance(town, strng):
    citywise = strng.split('\n')
    string_val = [i.split(":")[1] for i in citywise if i.split(":")[0]==town]
    if len(string_val)>0:
        array_val = {i.split()[0]:i.split()[1] for i in string_val[0].split(",")}
    else:
        array_val = {}
    if array_val!={}:
        return sum([(float(i)-mean(town,strng))**2 for i in array_val.values()])/len(array_val.values())
    else:
        return -1.0