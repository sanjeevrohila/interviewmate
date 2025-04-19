# Here we will provide the number to start and starting
# from that number you have to find all numbers, with
# them the bit wise AND operation is 0 
# a number length will be given to define the maximum number to generate

# Here we are going to use the functools.reduce function
# Sample input: [1,2,3,4]
# functools.reduce(lambda a, b : a*b, [1,2,3,4])
# reduces the list and returns the multiplication of all numbers.

from __future__ import annotations
import functools

def solution(num: int, length:int) -> list[int]:
    result: list[int] = [num]
    tries = num + 1
    while True:
        if len(result) == length:
            break
        temp = result + [tries]
        print(f"Try reduce on {temp=}")
        if functools.reduce(lambda x, y: x&y, temp) == 0:
            result.append(tries)
        
        tries = tries + 1
    return result


if __name__ == "__main__":
    res = solution(2,4)
    assert res == [2, 4, 5, 6]

    res = solution(5,3)
    assert res == [5, 8, 9]
