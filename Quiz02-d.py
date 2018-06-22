def infNorm(vector):

  '''
  This function calculates the infinity norm of a vector.  The infinity norm is the maximum absolute value of its components.  I used a for loop to take the absolute value of every element in vector, then another for loop to compare each element in the newvector in order to find the largest value.
  '''
  newvector = []
  for i in range(len(vector)):# for each iteration we take the absolute value of every element in vector
    newvector.append(abs(vector[i]))

  largest=newvector[0]

  for large in newvector:# for each iteration find the largest element in newvector
    if large > largest:
        largest=large

  print(largest)
      


#testvec = [1,2,3,-555]
#print(infNorm(testvec)) 