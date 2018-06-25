def normalize(vector):

  '''
  Input
  vector is a 1 x n in length
  
  Output
  newestvector is a 1 x n in length
  
  This function calculates the normalization of a vector with respect to the infinity norm. The infinity norm is the maximum absolute value of its components.  I used a for loop to take the absolute value of every element in vector, then another for loop to compare each element in the newvector in order to find the largest value.  From here we multiply 1/ largest times the original vector to get the normalized vector
  
  I used the code from part D to find the largest absolute number in the vector and then just added another for loop to apply the 1/ largest to the original vector.

  '''
  
  
  newvector = []

  for i in range(len(vector)):# for each iteration we take the absolute value of every element in vector
    newvector.append(abs(vector[i]))

  largest=newvector[0]

  for large in newvector:# for each iteration find the largest element in newvector if it finds a larger element it sets that to the largest and continues to compare elements for the range of elements in vector
    if large > largest:
        largest=large

  newestvector = []

  for j in range(len(vector)):#for each iteration multiply 1/largest times each element in vector
    newestvector.append(1/largest * vector[j])

  return newestvector
      
#testvec = [1,2,3,-55]
#print(normalize(testvec)) 
