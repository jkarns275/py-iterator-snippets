from typing import Iterator, List, Set, Dict, Tuple
import numpy as np

# List creation
square_numbers: List[int] = \
        [x * x for x in range(6)]

# Generator creation
square_numbers_generator: Iterator[int] = \
        (x * x for x in range(6))

# Set creation
square_numbers_set: Set[int] = \
        {x * x for x in range(6)}

# Dictionary / Map creation
square_numbers_map: Dict[int, int] = \
        {x: x * x for x in range(6)}

# Using a predicate
squared_even_numbers_generator: Iterator[int] = \
        (x * x for x in range(24) if x % 2 == 0)

# Comprehension with t
exponentiation_map: Dict[Tuple[int, int], int] = \
        { (base, exp): base ** exp for base in range(10) for exp in range(10)}

# Equal to the following
exponentiation_map2 = {}
for base in range(10):
    for exp in range(10):
        exponentiation_map2[(base, exp)] = base ** exp

assert exponentiation_map == exponentiation_map2

size = 5
matrix: List[List[float]] = np.random.rand(size, size)

# Nested iterators to flatten matrix
flattened_matrix: List[float] = \
        [matrix[row, column] for row in range(size) for column in range(size)]

# Same as
flattened_matrix2: List[float] = []
for row in range(size):
    for column in range(size):
        flattened_matrix2.append(matrix[row, column])

assert np.array_equal(flattened_matrix, flattened_matrix2)

# Nested iterators to construct a matrix from a sequence
reconstructed_matrix: List[List[float]] = \
        [[flattened_matrix[row * size + column] for column in range(size)] for row in range(size)]

# Same as
reconstructed_matrix2: List[List[float]] = []
for row in range(size):
    row_list = []
    for column in range(size):
        row_list.append(flattened_matrix[row * size + column])
    reconstructed_matrix2.append(row_list)

assert np.array_equal(reconstructed_matrix, reconstructed_matrix2)

# Original matrix is the same as the 
# flattened then reconstructed matrix
assert np.array_equal(matrix, reconstructed_matrix)

# Identity matrix using nested comprehension and an if expression
identity = [[1 if row == column else 0 for column in range(size)] for row in range(size)]

assert np.array_equal(np.identity(5), identity)
