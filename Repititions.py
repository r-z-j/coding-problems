"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n
 characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1 ≤ n ≤ 10^6

Example

Input:
ATTCGGGA

Output:
3
"""
n = input()
def reps(n):
    curr = n[0]
    count = 0
    maxCount = 0
    for i in n:
        if i == curr:
            count += 1
        else:
            count = 1
        if count > maxCount:
            maxCount = count
        curr = i
    return maxCount

print(reps(n))
