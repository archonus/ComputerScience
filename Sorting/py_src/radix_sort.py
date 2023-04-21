from typing import Any, Callable, List, TypeVar
T = TypeVar('T')

def _counting_sort(items : List[T], k, key : Callable[[T], int] = lambda x : x):
    """Sort on assumption that key(item) <= k for all items. Default is to expect a list of numbers"""
    n = len(items)
    counts = [0 for _ in range(k+1)]
    output = [None for _ in range(n)]

    for item in items:
        j = key(item)
        try:
            counts[j] += 1
        except IndexError: # If k is incorrect
            new_counts = [counts[i] if i <= k else 0 for i in range(j + 1)]
            k = j # Update the maximum range
            counts = new_counts
            counts[j] += 1
    
    for j in range(1,k+1):
        counts[j] += counts[j - 1] # Cumulative update
    
    for item in reversed(items):
        j = key(item)
        counts[j] -= 1
        output[counts[j]] = item

    return output

def get_digit(n, i):
    return n // (10**i)

def get_char(s, i):
    return ord(s[-(i + 1)])

def radix_sort(items : T, d : int, k : int, get_digit : Callable[[T, int], int] = get_digit):
    for i in range(d):
        key = lambda x : get_digit(x,i)
        items = _counting_sort(items,k,key)
    return items

if __name__ == '__main__':
    ls = [123,432,512,11,667,22,790,32,245,92,97,31,31,512,657,5]
    s = radix_sort(ls,3, 9)
    print(s)
    
