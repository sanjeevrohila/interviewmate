# The functools.reduce function enables you to apply a binary function to the elements of a sequence in a cumulative way.
# sample Input [1,2,3,4]
# Output 24

import functools

if __name__ == "__main__":
  
  input = [1,2,3,4]
  # Define a lambda function for the
  # functools.reduce to apply 
  multiply = lambda a,b:a*b
  
  resp = functools.reduce(multiply, input)
  assert resp == 24, "functools.reduce did not work as expected"
