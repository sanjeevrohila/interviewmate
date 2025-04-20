# The filter() function in Python is used to construct an
# iterator from elements of an iterable for which a function
# returns true. Here's a basic example:


if __name__ == "__main__":
  is_even = lambda x: x%2 == 0

  numbers = [1, 2, 3, 4, 5, 6]
  even_numbers = filter(is_even, numbers)

  print(list(even_numbers))  # Output: [2, 4, 6]
