import math

n = int(input("Enter a number: "))
root = int(math.sqrt(n))

count = 0

for i in range(2, root):
    if root % i == 0:
        count += 1

if count == 0 and root > 1:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")