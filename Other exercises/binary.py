""""A binary gap within a positive integer N is any maximal sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of N.
Write a function that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap. """

import re

# Forma 1

def solution(N):
    binary_form = str(bin(N)).replace('0b','')
    patern = '1?0+1'
    binary_gaps = re.findall(patern, binary_form)
    only_zeros = []
    length = []
    for i in range(len(binary_gaps)):
        only_zeros += [binary_gaps[i].replace('1', '')]
    for element in only_zeros:
        length += [len(element)]
    if len(length) == 0:
        max_length = 0
    else:
        max_length = max(length)
    return max_length


# Forma 2

def into_binary_list(n):
    residuals = []
    result = n
    while result >= 1:
        residuals += [result%2]
        result = result//2
    residuals.reverse()
    return residuals

def into_binary_string(n):
    binary = ''
    for element in into_binary_list(n):
        binary += str(element)
    return binary

def solution2(N):
    binary_form = into_binary_string(N)
    patern = '1?0+1'
    binary_gaps = re.findall(patern, binary_form)
    only_zeros = []
    length = []
    for i in range(len(binary_gaps)):
        only_zeros += [binary_gaps[i].replace('1', '')]
    for element in only_zeros:
        length += [len(element)]
    if len(length) == 0:
        max_length = 0
    else:
        max_length = max(length)
    return max_length