
n=5

for row in range(n):
    for col in range(n-1-row):
        print(" ",end="")
    for col in range(row+1):
        print("*", end= " ")
    print()


for row in range(n):
    for col in range(row):
        print(" ",end="")
    for col in range(n-row):
        print("*", end= " ")
    print()
 
