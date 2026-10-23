#create a function without return

def place_order(item):
    print(f'Place order:your placed order is:{item}')
# eggs>=4
# tot = base_price + 5 * 1.15 
def Calc_total(item):
    
    base_price = 25.5
    VAT = 0.15
    tot = (base_price + len(item)) * 1.15
    return tot
#create a function   
def get_order():
    print('preparing order')
    return 'Collect the order'
myfood = input(' what would you like: ')
place_order(myfood)

#calling a function
#msg = get_order()
#print(msg)

print(get_order())
order_total = Calc_total(myfood)
#print(f'Your oder costs: R{order_total:.2f}')
print(f'your order costs: R{round(order_total,2)}')









    
     
    