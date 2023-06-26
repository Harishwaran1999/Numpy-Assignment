#1.Create a null vector of size 10 but the fifth value which is 1.

import numpy as np

null_vector = np.zeros(10)  
null_vector[4] = 1  

print(null_vector)
[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]


#2.Create a vector with values ranging from 10 to 49.

import numpy as np

vector = np.arange(10, 50)
print(vector)
[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]




#3.Create a 3x3 matrix with values ranging from 0 to 8

import numpy as np

matrix = np.arange(9).reshape(3, 3)
print(matrix)
[[0 1 2]
 [3 4 5]
 [6 7 8]]


#4.Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np

input_list = [1, 2, 0, 0, 4, 0]


# Convert the list to a NumPy array
arr = np.array(input_list)

nonzero_indices = np.nonzero(arr)
print(nonzero_indices)
(array([0, 1, 4], dtype=int64),)



#5.Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np


# Create a 10x10 array with random values
random_array = np.random.rand(10, 10)

# Find the minimum and maximum values
minimum_value = np.min(random_array)
maximum_value = np.max(random_array)

print("Random Array:")
print(random_array)
print("Minimum Value:", minimum_value)
print("Maximum Value:", maximum_value)
Random Array:
[[2.68431118e-01 3.29886676e-01 7.43538980e-01 9.50842791e-01
  5.14311735e-01 1.74582601e-01 7.90680868e-01 3.42392655e-01
  8.76466537e-01 7.95783788e-01]
 [2.90636591e-01 7.12184917e-01 1.04724919e-01 9.26848407e-01
  8.15408769e-02 6.88199355e-01 7.30127599e-01 4.11979398e-01
  7.88252252e-02 6.04812502e-01]
 [9.15807074e-01 3.78137632e-01 3.26540605e-01 9.86871392e-01
  1.98288880e-01 8.42333442e-01 9.62415285e-01 1.80199970e-01
  1.41788461e-01 1.12070559e-01]
 [3.89671812e-01 6.52509872e-01 1.79167169e-02 1.52881851e-01
  1.77476744e-01 3.53529478e-01 4.71250210e-01 4.82548064e-01
  7.20742969e-02 6.90424329e-01]
 [5.50417961e-02 1.22478747e-01 2.51137302e-01 7.40031088e-01
  5.09015298e-01 9.36383047e-01 1.75496037e-01 3.60375320e-01
  8.32456537e-01 4.72597826e-01]
 [4.08898988e-01 8.35848036e-01 6.36891149e-01 6.01865799e-02
  3.27805304e-01 1.36271541e-01 1.77541432e-01 6.69331588e-01
  5.61524118e-01 4.54081036e-01]
 [8.83860085e-01 9.32301342e-01 5.05212002e-01 7.29353977e-01
  6.50653640e-02 7.90185322e-01 1.27244533e-01 4.55009861e-04
  2.28208568e-01 8.58017137e-01]
 [4.94303845e-01 3.49038148e-01 1.19855297e-01 8.39357632e-01
  1.57518528e-01 8.44314216e-01 3.77817479e-03 1.17015013e-01
  4.84860872e-01 9.60907140e-01]
 [6.09074752e-01 1.13913933e-01 3.79744469e-01 8.63505085e-02
  2.75565683e-01 2.23734825e-01 9.95716829e-01 2.21489795e-01
  2.97831534e-01 1.77835785e-01]
 [4.40515724e-01 2.39283468e-01 7.74281498e-01 8.39940628e-01
  9.44710545e-01 1.36626424e-01 9.63257982e-01 5.33269005e-01
  5.66761124e-01 1.06365163e-01]]
Minimum Value: 0.00045500986114555
Maximum Value: 0.9957168294501864



#6.Create a random vector of size 30 and find the mean value.
import numpy as np

# Create a random vector of size 30
random_vector = np.random.rand(30)

# Calculate the mean value
mean_value = np.mean(random_vector)

print("Random Vector:", random_vector)
print("Mean Value:", mean_value)
Random Vector: [0.90248519 0.13240902 0.69267176 0.17602618 0.88395937 0.58327412
 0.1906705  0.31697159 0.53226419 0.07018473 0.13290594 0.24607984
 0.20979571 0.96640268 0.23101171 0.63024173 0.36463814 0.62265944
 0.68344248 0.48975277 0.35642857 0.62205469 0.17636001 0.03678057
 0.77024171 0.42261773 0.21956422 0.14811707 0.25999555 0.72687009]
Mean Value: 0.42656257644294426