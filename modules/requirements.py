

def vector_requirements (vector):

    if str(type(vector)) != "<class 'list'>":
        print ('VectorErrorType: Verify input type.')
        print ('_____________________%program finished%______________________')
        return 0
    
    if len(vector)== 0:
        print ('VectorError: Attention! Vector is empty!')
        print ('_____________________%program finished%______________________')
        return 0
    elif  str(type(vector[0])) == "<class 'list'>": 
        print ('VectorError: Attention! The input is wrong! It must be a vector, not a matrix')
        print ('_____________________%program finished%______________________')
        return 0

    vector_range_max = 15
    vector_range_min = 0
    
    for element in vector:
        if element < vector_range_min or element > vector_range_max:
            print ('VectorError: Attention! Elements in vector are not in range!')
            print (' 1th result ->  ', element)
            print ('_____________________%program finished%______________________')
            return 0
    
    return 1

def matrix_requirements (matrix):
    
    if str(type(matrix)) != "<class 'list'>":
        print ('MatrixErrorType: Verify input type.')
        print ('_____________________%program finished%______________________')
        return 0
    
    if len(matrix)== 0:
        print ('MatrixError: Attention! Matrix is empty!')
        print ('_____________________%program finished%______________________')
        return 0

    elif len(matrix[0]) == 0:
        print ('MatrixError: Attention! Matrix is empty!')
        print ('_____________________%program finished%______________________')
        return 0
    
    return 1
