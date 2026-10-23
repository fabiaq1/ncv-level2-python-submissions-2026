import math
#Calculate cube of five
tot = 0
number = int(input('Enter number'))
for n in range(1,number + 1):
    #display cube and its calculation
    
    print(pow(n,3),end="")
    #calc total and display it
    tot = tot + n
    print('total: ', tot)
#continue

#print('good')
