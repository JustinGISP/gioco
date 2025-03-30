'''
stats

This module contains functions for performing statistical analysis on sets if numerical values

'''
from collections import Counter

# Define common errors
emptyListError = "List of numbers cannot be empty"

def mean(nums):
    ''' Calculates the mean of a set of numbers'''
    if not nums:
        raise ValueError(emptyListError)
    
    return sum(nums) / len(nums)

def median(nums):
    ''' Calculates the median of a set of numbers'''
    if not nums:
        raise ValueError(emptyListError)
    
    sort = sorted(nums)
    n = len(sort)
    mid = n // 2

    if n % 2 == 0:
        return (sort[mid - 1] + sort[mid]) / 2
    else:
        return sort[mid]
    
def mode(nums):
    ''' Calculates the median of a set of numbers'''
    if not nums:
        raise ValueError(emptyListError)
    
    counts = Counter(nums)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]

    if len(modes) == len(nums):
        raise ValueError("No mode found, all values appear equally.")
    return modes

def range(nums):
    '''Calculates the range of a set of numbers'''
    if not nums:
        raise ValueError(emptyListError)
    
    return max(nums) - min(nums)
