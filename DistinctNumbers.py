args = int(input())

input_array = list(input().split())

def distinct_numbers(arr):
    if len(arr) == 0:
        print(0)
        return

    if len(arr) == 1:
        print(1)
        return

    arr.sort()
    count = 1

    j = arr[0]
    for i in arr:
        if i != j:
            count += 1
        j = i
    print(count)

distinct_numbers(input_array)
