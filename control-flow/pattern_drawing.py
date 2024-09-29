size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    col = 0
    while col < size:
        print('*', end='') 
        col += 1 
    print() 
    row += 1  
