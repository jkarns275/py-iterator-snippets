from typing import Iterator, List

my_numbers = [0, 1, 2, 3, 4, 5, 6]

##
# Iterable Objects
##
class SquareNumbersObject(Iterator):

    def __init__(self, numbers: List[float]):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> float:
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value * value
        else:
            raise StopIteration()

squared_standard = list(SquareNumbersObject(my_numbers))

##
# Generator
##
def square_numbers_generator(numbers: List[float]) -> Iterator[float]:
    index = 0

    while index < len(numbers):
        value = numbers[index]
        yield value * value
        index += 1

squared_gen = list(square_numbers_generator(my_numbers))

##
# Comprehension
##
def square_numbers_comprehension(numbers: List[float]) -> List[float]:
    return [x * x for x in numbers]

squared_comprehension = square_numbers_comprehension(my_numbers)

print(squared_gen)
print(squared_standard)
print(squared_comprehension)

assert  squared_gen  == squared_standard and \
        squared_gen == squared_comprehension

##
# Infinite generator example
## 
import numpy as np

# Generates noise with dimensions given by shape
def noise(shape):
    rng = np.random.default_rng()
    while True:
        yield rng.random(size=shape)
