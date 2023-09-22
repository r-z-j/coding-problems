n = int(input())

def beautiful_permutation(n):
    if n == 1:
        print("1")
    elif n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        even_nums = list(range(2, n+1, 2))
        odd_nums = list(range(1, n+1, 2))
        permutation = even_nums + odd_nums
        print(" ".join(map(str, permutation)))

beautiful_permutation(n)
