#define_array
marks = []
mark= int(input('Enter marks or enter -1 to stop'))
i = 0

while mark != -1:
    marks.append(mark)
    #marks[i] = mark
    i = i+1
 
    mark= int(input('Enter marks (or enter -1 to stop)'))
 

print(f'our list has {len(marks)} elements')

## get the sum of all marks
sum=0
for x in range(len(marks)):
    mark= marks[x]
    sum = sum + mark
    print(f'The sum of all marks = {sum}')
    
    
## get average of all marks   
total=0
for x in range(len(marks)):
    mark = marks(x)
    total = total + mark
    average = total / len(marks)
    print(f'The sum of all marks = {average}')

    