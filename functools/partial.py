import functools

# Define a simple function that takes three arguments
def multiply(x: int, y: int, z: int) -> int:
  return x * y * z

if __name__ == "__main__":
  # Create a new function with the first argument preset to 2
  multiply_by_two = functools.partial(multiply, 2)
  
  # Now you can call the new function with only the remaining arguments
  result = multiply_by_two(3, 4)  # Equivalent to multiply(2, 3, 4)
  
  print(f"Result: {result}")  # Output: Result: 24
