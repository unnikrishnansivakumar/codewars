def digital_root(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    if len(str(sum))==1:
        return sum
    else:
        return digital_root(sum)
      