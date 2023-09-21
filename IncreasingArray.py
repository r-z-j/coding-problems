n = input()

arr = [int(x) for x in input().split()]

count = 0
prev = arr[0]
for i in arr[1:]:
    if prev > i:
        count += prev - i
    else:
        prev = i
print(count)

