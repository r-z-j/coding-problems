def find_number(y, x):
    if y > x:
        if y % 2 == 0:
            return y * y - x + 1
        else:
            return (y - 1) * (y - 1) + x
    else:
        if x % 2 == 1:
            return x * x - y + 1
        else:
            return (x - 1) * (x - 1) + y

t = int(input())
"""
for _ in range(t):
    y, x = map(int, input().split())
    result = find_number(y, x)
    print(result)
"""

spiral = [[0 for _ in range(t)] for _ in range(t)]

for i in range(t):
    for j in range(t):
        spiral[i][j] = find_number(i+1, j+1)

for i in spiral:
    for j in i:
        print(repr(j).rjust(6), end=" ")
    print()

