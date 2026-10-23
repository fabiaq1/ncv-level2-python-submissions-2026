##Combination of functions and list array
marks = []
def getmarks():
    #define_array
    
    mark= int(input('Enter marks or enter -1 to stop'))
    ##i = 0
    while mark != -1:
        marks.append(mark)
    #marks[i] = mark
    ##i = i+1
        mark= int(input('Enter marks (or enter -1 to stop)'))
 
def print_list_size(marks):
 
    print(f'our list has {len(marks)} elements')

def print_marks(marks):
    ## get the sum of all marks
    sum=0
    for x in range(len(marks)):
        mark = marks[x]
        sum = sum + mark
    return sum
print(f'The sum of all marks = {sum}')
 
 
## get average of all marks
average=0
total=0
for x in range(len(marks)):
        mark = marks(x)
        total = total + mark
        average = total / len(marks)
print(f'The sum of all marks = {average}')

def determine_highes(marks):
    highest=0
    for i in range(len(marks)):
        current_mark = marks[i]
        if (current_mark > highest):
            highest = current_mark
print(f'The sum of all marks = {sum}')

menu = 'Press 1: Capturing marks\n'
menu += 'Press 2: Check number of marks\n'
menu += 'Press 3: to Calculate sum marks\n'
menu += 'Press 4: To find highes mark\n'
menu += 'Press -1: To exit marks\n'
print(menu)
choice = 0
entered_marks = []
if choice == 1:
    entered_marks = getmarks()
    print(entered_marks)
elif choice == 2:
    print_list_size(entered_marks)
elif choice == 3:
    calc_sum = print_marks(entered_marks) 
elif choice == 4:
    determine_highes(entered_marks)
else:
   print('its not on the menu list')
   
  

    
    
