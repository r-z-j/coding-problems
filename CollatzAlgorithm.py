num = input().strip()

def collatz(n):
    try:
        n = int(n)
        steps = 0 
        while n != 1:
            steps += 1
            print(n, end=" ")
            if n % 2 == 0:
                n = int(n / 2)
            else: 
                n = n * 3 + 1
        print(n)
    except ValueError:
        print('Error you did not enter a number')

collatz(num)
