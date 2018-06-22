def scalarVecMulti(scalar,vector):

  '''
  Input
  scalar should be a number
  vector should be a 1 x n in length
  
  Output
  newvector should be a 1 x n in length

  This function inputs a scalar and a vector, then multiplies the scalar to every element in the vector for the length of the vector.

  '''
  
  cV = len(vector[0])
  if cV > 1
    print("Invalid Input")
    return
  
  newvector = []

  for i in range(len(vector)):
    newvector.append(scalar * vector[i])
# for each iteration the vector element is multiplied by the scalar and put into the new vector
  return newvector
  
#testscalar = 8      
#testvec = [1,2,3]

#print(scalarVecMulti(testscalar,testvec)) 
