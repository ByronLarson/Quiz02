def infNorm(vector):

  '''
  Input
  vector should be 1 x n in length
  
  Output
  largest should be a scalar
  
  This function calculates the infinity norm of a vector.  The infinity norm is the maximum absolute value of its components.
  I used a for loop to take the absolute value of every element in vector, then another for loop to compare each element in the newvector in order to find the largest value.
  '''
  # for each iteration we take the absolute value of every element in vector and put these new absolute elements into a newvector
  newvector = []
  for i in range(len(vector)):
    newvector.append(abs(vector[i]))

  largest=newvector[0]
  # for each iteration find the largest element in newvector.  This loop compares the first element to the next element and if it is larger it replaces it as the largest element then contimes to compare numbers for the length of the vector
  for large in newvector:
    if large > largest:
        largest=large

  return largest
      
#testvec = [1,2,3,-555]
#testvec0 = apple

#print(infNorm(testvec)) 
