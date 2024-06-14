n=5

for row in range(n):
    for col in range(row):
        print('*',end='')
    print()
     
    
n=5 
for row in range(n):
    for col in range(row):
        print(row,end='')
    print()

n=5

for row in range(n):
    for col in range(row):
        print(col,end='')
    print()

num = 1

for row in range(5):
    for col in range(row):
        print(num,end='')
        num = num+1
    print()

