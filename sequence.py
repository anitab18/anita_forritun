n = int(input("Enter the length of the sequence: ")) 
i = 1
first = 1
second = 2
third = 3


while i <= n:
    i += 1
    print(first)
    first, second, third = second, third, first + second + third