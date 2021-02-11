
#    ---   Question 6   ---
#
# Create a function squares() which for any given python list 
# x of numeric values returns the list of squares of components 
# of vector x.
#-------------------------------------------------------------
# For example, if x = [-2, 3, 0], your function should return

#   squares(x)
#   [4,9,0]

# If x = [2, -5, 4, 3, 1, 1, -3], your function should return

#   squares(x)
#   [4, 25, 16, 9, 1, 1, 9]
#-------------------------------------------------------------

# Define the function "squares"
def squares(x):
    # givena list x, initialize list
    list = []
    # loop through given list 
    for i in x:
        #repace each item in the list with its squared value
        list.append(i**2)
    return(list)

#test list
x = [-2, 3, 0]

#call function
squares(x)
#-------------------------------------------------------------

#   ---   Question 7   ---
#
# Create a function sumsquares() which, for a whole number  𝑛≥0 , 
# returns the sum of squares of all the whole numbers up to and 
# including  𝑛 . If  𝑛  is not a whole number (i.e. not a non-
# negative integer), use the following statement in your code 
# to report the error.

#   raise ValueError("Sorry, n must be a whole number!")

# -------------------------------------------------------------
#Here are some examples:

#   sumsquares(0)
#   0

#   sumsquares(2)
#   5

#   sumsquares(2.3)
#   ValueError: Sorry, n must be a whole number!
#-------------------------------------------------------------

def sumsquares(n):
# Given list n
  # check for whole number
  if(n<0 or n-(int(n)) != 0):
    raise ValueError("Sorry, n must be a whole number")
  # initialize value to store the summs
  sum = 0
  # loop through the given list
  for i in range(n+1):
    #sum the squares
    sum = sum + i**2
  #return result 
  return sum
  
print(sumsquares(0))
print(sumsquares(2))
print(sumsquares(2.3))
