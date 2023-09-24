n, x = map(int, input().split())
p = list(map(int, input().split()))

"""
n: number of children
x: max allowed weight
p: list of weights of children
"""

p.sort()

result = 0
i = 0
j = n - 1
while i <= j:
    if p[i] + p[j] <= x:
        i += 1
        j -= 1
    else:
        j -= 1
    result += 1

print(result)

