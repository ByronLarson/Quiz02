def scalarVecMulti(scalar,vector):
  '''
  Inputs:
    A- scalar with dimensions row-scalar x column-scalar
    B- scalar with dimensions row-vector x 1
  Output:
    C - vector with dimensions row-scalar x 1

    I modified the limitations for my matrix times a vector code to only accept scalars and vector as inputs

  Details:
    This is the scalar times vector multiplication algorithm.
    For each scalar row, each vector columns = 1, and con to 0. con is the placeholder scalar to add each repition. Then for each scalar     column, add scalar[i][k]*vector[k] to con. Then set container[i][1] = con.
    The result is a scalar rows in the scalar by 1.
  '''

  rA = len(scalar)# find the number of rows in scalar A
  cA = len(scalar[0])# find the number of columns in scalar A
  rB = len(vector)# find the number of rows in vector B
  cB = len(vector[0])# find number of columns in vector B; should be 1
  if(vector):
    if(cB > 1) or type(vector) == str:
      print("invalid inputs")
      return

  if(scalar):
    if(type(scalar) == str or rA > 1 or cA > 1):
      print("invalid inputs")
      return

  #initialize a container to be a scalar  with 0s for all entries.
  container = [[0]*1 for row in range(rA)]


  for i in range(rA):
    # iterate through rows of the scalar
    for j in range(cB):
      # iterate through columns of vector whish should be 1
      con= 0
      for k in range(cA):
        #iterate through columns of the scalar
        con +=  scalar[i][k]*vector[k][j]
        #use += to add con + calculated value to placeholder scalar
      container[i] = con #final scalar will be the number of rows by 1 column
  return container


testscalar01 = [[12]]
                
                
testscalar02 = [1,2,3]
testscalar03 = 'this is a test'

testVector01 = [[5],
                [8],
                [1]]
testVector02 = [[12,7,3],
                [4 ,5,6],
                [7 ,8,9]]
testVector03 = True

# These are test cases for the function matVec. All but one of the tests should be commented out at a time so that we can see how each pair of inputs effects the output. 

print(scalarVecMulti(testscalar01,testVector01))
#print(matVec(testscalar02,testVector02))
#print(matVec(testscalar03,testVector03)) 
