'''You want to go up a ﬂight of stairs that has n steps. You can either take 1
 or 2 steps each time.

 How many diﬀerent ways can you go up this ﬂight of
 stairs?

 Write a function count_stair_ways that solves this problem. Assume
 n is positive.'''

def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4

    >>> count_k(4, 4)
    8

    >>> count_k(10, 3)
    274

    >>> count_k(300, 1) # Only one step at a time
    1
    """

    if n == 0:
        return 1
    elif n<0:
        return 0
    elif k<0
    else:
        total, i = 0,1
        while i <= k:
            total+= count_k(n-i,k)
            i += 1
        return total

def even_weighted(lst):
    '''keeps only the even-indexed elements of lst and multiplies them by their corresponding index.'''
    return [lst[i]*i for i in range(len(lst)) if i%2==0 ]

def count_digits(n):
'''
>>> count_digits(4)
1
>>> count_digits(12345678)
8
>>> count_digits(0)
0
'''
    if n == 0:
        return 0
    elif n<10:
        return 1
    else:
        return count_digits(n%10)+count_digits(n//10)
