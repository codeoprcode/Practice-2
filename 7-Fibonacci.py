
itr = 2
a = 0
b = 1

n = int(input("Please enter number of sequence: "))

for i in range(n):

    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    elif n <= 0:
        print("Please enter psitive number")
    elif n > 2:
        num_new = a + b
        print (num_new)
        a = b
        b = num_new


 