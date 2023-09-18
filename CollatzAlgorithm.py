import tracemalloc

print("Enter a number: ")
num = input()
steps = 0

def collatz(n):
    global steps 
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
