fullname = input("Enter fullnames: ")
staffnumber= (input("Enter staffnumber: "))
level = int(input("Enter level: "))

if not (fullname.isalpha()):
    print("full name must contain alphabets")
elif  (staffnumber.isdigit()):
    print("staff number should be numeric value")
else:
    
     print("Full name:", fullname )
     print("staff number:", staffnumber )
     print("staff number:", level )