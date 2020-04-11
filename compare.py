import numpy as np

def find_missing_number(numbers):
  snumbers = np.sort(np.array(numbers))
  if 1 not in snumbers:
    return 1
  elif True in (snumbers[1:]-snumbers[:-1]==2):
    return snumbers[np.where(snumbers[1:]-snumbers[:-1]==2)][0]+1
  else:
    return snumbers[-1]+1


if __name__=='__main__':
  print(find_missing_number([1,2,3,4]))
