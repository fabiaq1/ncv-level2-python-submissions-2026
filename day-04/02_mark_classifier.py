mark=int(input("Please enter mark: "))

         
if mark<0 or mark>100:
    print("invalid mark")
    
elif mark >= 0 and mark<=39:
   print("Not achieved")
   
elif mark >= 40 and mark<=49:
   print("Not yet competent")
   
elif mark >= 50 and mark<=69:
   print("Competent")
   
elif mark >= 70 and mark<=79:
   print("Highly competent")
   
elif mark >= 80 and mark<=100:
   print("Outstanding")
   
else:
    print("invalid mark")
    