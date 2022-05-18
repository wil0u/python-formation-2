# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:12:55 2020

@author: RND
"""

import itertools as it



# Combinations & Permutations
list(it.combinations([1, 2, 3], 2))
list(it.combinations_with_replacement([1, 2], 2))
list(it.permutations('abc’))



# Zip & zip_longest
x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c’]

list(zip(x, y))
list(it.zip_longest(x, y))



# Sequence & Recurrence
evens_counter = it.count(step=2)
list(next(evens_counter) for i in range(5))

odds_counter = it.count(start=1, step=2)
list(next(odds_counter) for i in range(5))


list(it.accumulate([1, 2, 3, 4, 5]))
import operator
list(it.accumulate([1, 2, 3, 4, 5], operator.add))  #(add(3, 3) = 6)
list(it.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min))
list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: (x + y) / 2))




# Products
list(it.product([1, 2], ['a', 'b']))

# Slicing
list(it.islice('ABCDE', 4))                     # Slice from beginning to index 3
list(it.islice([1, 2, 3, 4, 5], 0, 5, 2))       # Slice from beginning to index 4, in steps of 2

# Chain
list(it.chain('ABC', 'DEF'))
list(it.chain([1, 2], [3, 4, 5, 6], [7, 8, 9]))


