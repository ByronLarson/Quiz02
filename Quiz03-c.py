def scalarVecMulti(scalar,vector):

  '''

  This function inputs a scalar and a vector, then multiplies the scalar to every element in the vector for the length of the vector.

  '''
  newvector = []

  for i in range(len(vector)):
    newvector.append(scalar * vector[i])
# for each iteration the vector element is multiplied by the scalar and put into the new vector
  return newvector
  
#testscalar = 8      
#testvec = [1,2,3]

#print(scalarVecMulti(testscalar,testvec)) 
