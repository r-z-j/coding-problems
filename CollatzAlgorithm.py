import tracemalloc

print("Enter a number: ")
num = input()

def collatz(n):
    steps = 0 
    while n != 1:
        steps += 1
        print(steps, "\t", n)
        if n % 2 == 0:
            n = int(n / 2)
        else: 
            n = n * 3 + 1

tracemalloc.start()

collatz(int(num))

stats = tracemalloc.get_traced_memory()
print("Memory usage:", stats[0] / (1024 * 1024), "MB")

tracemalloc.stop()
