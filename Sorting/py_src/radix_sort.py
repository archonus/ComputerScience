from typing import Any, Callable, List, TypeVar
T = TypeVar('T')

def _counting_sort(items : List[T], k, key : Callable[[T], int] = lambda x : x):
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

if __name__ == '__main__':
    ls = [3,4,5,1,6,2,7,3,2,9,9,3]
    s = _counting_sort(ls, 9)
    print(s)
    
