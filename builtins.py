from typing import List, Iterable, Dict, Set

## 
# Zip and Enumerate
##

# Columns of a CSV file or something
first_names: List[str] = \
        ['Josh',  'Jeff',  'Jessica', 'John', 'Joanne']
last_names: List[str] = \
        ['Karns', 'Salad', 'Brown',   'Doe',  'Lee']

full_names: List[str] = \
        [f'{first} {last}' for first, last in zip(first_names, last_names)]

index_to_full_name: Dict[int, str] = \
        { index: name for index, name in enumerate(full_names) }


##
# List, Dict, and Set
##

set_of_first_names: Set[str] = \
        set(first_names)
n_to_n_squared: Dict[int, int] = \
        dict([(x, x * x) for x in range(10)])

index_to_full_name2: Dict[int, str] = \
        dict(( (index, name) for index, name in enumerate(names) ))

assert index_to_full_name == index_to_full_name2



def square(x: int) -> int:
    return x * x

squares: List[int] = \
        list(map(square, range(10)))

squares_lambda: List[int] = \
        list(map(lambda x: x * x, range(10)))

squares_imperative: List[int] = []
for x in range(10):
    squares_imperative.append(x * x)

assert  squares == squares_lambda and \
        squares == squares_imperative


##
# Filter
##

def is_odd(x: int) -> bool:
    return x % 2 == 1

numbers: Iterable[int] = range(10)
odd_numbers: Iterator[int] = \
        filter(is_odd, numbers)
odd_numbers_list: List[int] = \
        list(filter(is_odd, numbers))

##
# Reduce
##

# Sum of numbers using reduce
assert sum(range(10)) == reduce(lambda x, y: x + y, range(10))

# Product of numbers
product = lambda sequence: reduce(lambda x, y: x * y, sequence)
assert product([1, 2, 3, 4]) == 1 * 2 * 3 * 4

# Comma separate strings
comma_separate = lambda sequence: reduce(lambda x, y: f'{x}, {y}', sequence)
assert comma_separate(range(4)) == '0, 1, 2, 3'


##
# Reversed
##

# Iterate through a list backwards
first_names_reversed = [name for name in reversed(first_names)]
assert first_nam
