# The functools.reduce function enables you to apply a binary function to the elements of a sequence in a cumulative way.
# sample Input [1,2,3,4]
# Output 24
from __future__ import annotations
import functools
import typing

def demo_reduce(function: typing.Callable , input: list[int]) -> int:
  return functools.reduce(multiply, input)

if __name__ == "__main__":
  
  input = [1,2,3,4]
  # Define a lambda function for the
  # functools.reduce to apply 
  multiply = lambda a,b:a*b
  
  resp = demo_reduce(multiply, input)
  assert resp == 24, "functools.reduce did not work as expected"
