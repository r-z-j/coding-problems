n, q = map(int, input().split())
array_values = list(map(int, input().split()))
prefix_sum = [0] * n
prefix_sum[0] = array_values[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + array_values[i]

result = []
for _ in range(q):
    a,b = map(int, input().split())
    range_sum = 0
    if a == 1:
        range_sum = prefix_sum[b-1]
    else:
        range_sum = prefix_sum[b-1] - prefix_sum[a-2]
    result.append(range_sum)


for r in result:
    print(r)

