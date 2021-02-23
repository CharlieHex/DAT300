# importing library numpy
import numpy as np
import types

#    ---   Question 1   ---
#
# Consider the function  𝑓(𝑥,𝑦)=𝑥2sin3𝑦+2𝑦3𝑥√ .
#---------------------------------------------------------
#Define Python function gradf(x,y) which for each point (x,y) with  𝑥>0  gives the gradient  ∇𝑓(𝑥,𝑦)=(𝑓𝑥(𝑥,𝑦),𝑓𝑦(𝑥,𝑦))  as Python's tuple object.

#Use attribute pi from numpy for the value of  𝜋 . So, if numpy is imported as np, use np.pi
#-------------------------------------------------------------

# Define the function "gradf"
def gradf(x,y):
    # Partial Derivative with respect to x
    pDerX = (2 * x * np.sin(y)**3) - (y**3 / x**1.5)
    # Partial Derivative with respect to y
    pDerY = (3 * (x ** 2) * (np.sin(y)**2) * np.cos(y)) + (6 * (y ** 2) / np.sqrt(x))
    # Create Tuple
    gradient = (pDerX,pDerY)
    return gradient

# Call function
print("Gradient of f(x , y) at (2 , pi) = " , gradf(2 , np.pi))
#-------------------------------------------------------------

