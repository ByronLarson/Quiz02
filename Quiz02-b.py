def vecSubtract(vector01,vector02):

  '''
  In the vecSubtract function two vector lengths are compared, if they are the same length then they can be subtracted.  Each element from their respective places in each row is subtracted from each other then returned into a new vector containing the result
  '''

  if len(vector01)==len(vector02):# checks to see that the vectors are the same length
    newvec = []
    for i in range(len(vector01)):
      newvec.append(vector01[i] - vector02[i])# for each iteration each vector is subtracted from one another
    return newvec
  else:
    print("invalid inputs")