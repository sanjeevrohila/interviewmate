# The map () function returns a map object(which is an iterator) 
# of the results after applying the given function to each item
# of a given iterable (list, tuple, etc.).

# >>> input = [1,2,3,4,5]
# >>> square_function = lambda x: x*x
# >>> for ele in map(square_function, input):
# ...     print(ele)
# ...     
# 1
# 4
# 9
# 16
# 25
# >>> 

if __name__ == "__main__":
  input = [1,2,3,4,5]
  square_function = lambda x: x*x

  for ele in map(square_function, input):
    print(ele)
