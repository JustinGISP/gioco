'''
stats

This module contains functions for performing statistical analysis on sets if numerical values

'''
from collections import Counter

# Define common errors
emptyListError = "List of numbers cannot be empty"


def calc_mean(nums):
    ''' Calculates the mean of a set of numbers'''
    if not nums:
        raise ValueError(emptyListError)
    
    return sum(nums) / len(nums)


def calc_median(nums):
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
    

def calc_mode(nums):
    ''' Calculates the median of a set of numbers'''
    if not nums:
        raise ValueError(emptyListError)
    
    counts = Counter(nums)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]

    if len(modes) == len(nums):
        raise ValueError("No mode found, all values appear equally.")
    return modes


def calc_range(nums):
    '''Calculates the range of a set of numbers'''
    if not nums:
        raise ValueError(emptyListError)
    
    return max(nums) - min(nums)


def calc_std_dev(dataset, sample=False, round_to=None):
    '''
    Calculates the standard deviation of a list or tuple
    Args:
        dataset: list or tuple of numerical values
        sample: use sample (True) or population (False) - defaults to population
        round_to: number of decimal spaces to round the answer - defaults to None
    '''
    # Type check
    if not isinstance(dataset, (list, tuple)):
        raise TypeError("Input must be a list or tuple of numeric values.")

    # Empty check
    if len(dataset) == 0:
        raise ValueError("Input dataset cannot be empty.")

    # Value checks
    for x in dataset:
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise ValueError(f"Invalid value detected: {x}. All elements must be numeric and not boolean.")
        if x != x or x == float("inf") or x == float("-inf"):
            raise ValueError(f"Invalid numeric value: {x}. NaN and infinities are not allowed.")

    # Calculate mean
    mean = calc_mean(dataset)

    # Calculate variance
    squared_diffs = [(x - mean) ** 2 for x in dataset]
    divisor = len(dataset) - 1 if sample else len(dataset)
    if divisor <= 0:
        raise ValueError("At least two dataset points are required for sample standard deviation.")
    variance = sum(squared_diffs) / divisor

    result = variance ** 0.5

    return round(result, round_to) if round_to is not None else result
