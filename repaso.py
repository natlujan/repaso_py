import numpy as np
#ndarray

data = np.array([ [1,2], 
                  [3,4], 
                  [5,6],
                  [7,8] ], dtype = np.float64)
print(data)
print( "Tipo de dato: " + str(type(data)) )
print( "Shape: " + str(data.shape) )
print( "Size: " + str(data.size))
print( "Ndim: " + str(data.ndim))
print( "Dtype: " + str(data.dtype))

#data = np.array(data, dtype = np.int64)
data = data.astype(np.int64)
print( "Dtype modificado: " + str(data.dtype))
