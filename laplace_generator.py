# Importing predefined Python Libraries
from random import random
from math import log

# Function generating exponential sample value
def exponential_sample_value(mean_value):
    return -mean_value*log(random())

# Function generating laplace value
def laplace_value(scale_value):
    # Calling exponential generating function to get laplace value
    expo_1 = exponential_sample_value(scale_value)
    expo_2 = exponential_sample_value(scale_value)
    print('\n')
    print('The two independent Exponential sample values for the given scale value are:')
    # Printing both the exponential sample values
    print('First Exponential Sample Value: ' + str(expo_1))
    print('Second Exponential Sample Value: ' + str(expo_2))
    # Calculating Laplace value using the difference of both exponential sample values
    laplace_val = expo_1-expo_2
    print('\n')
    print('The difference between the both generated exponential values is used to generate the Laplace value')
    # Printing the Laplace Value
    print('Laplace Value for ' + str(var) + ' is: ' + str(laplace_val))
    return laplace_val

# Taking scale value from the user as input
var = int(input("Enter value of scale:"))
# Calling Laplace value generation function
laplace_value(var)

