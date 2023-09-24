n, m, k = map(int, input().split())
"""
n = number of applicants
m = number of available apartments
k = max allowed difference in size
"""

aplicant_sizes = list(map(int, input().split()))
apartment_sizes = list(map(int, input().split()))

aplicant_sizes.sort()
apartment_sizes.sort()

assigned_applicants = 0
i = 0
j = 0

while i < n and j < m:
    if abs(aplicant_sizes[i] - apartment_sizes[j]) <= k:
        assigned_applicants += 1 
        i += 1
        j += 1
    elif aplicant_sizes[i] > apartment_sizes[j]:
        j += 1
    else:
        i += 1 
print(assigned_applicants)
