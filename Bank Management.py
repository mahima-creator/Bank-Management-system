accounts={}
while True:
    print("\n ===== BANK MANAGEMENT SYSTEM =====")
    print("1.Create Account")
    print("2.Check Balance")
    print("3.Exiit")
    choice=int(input("Enter your choice:"))
    if choice==1:
           acc_no=int(input("Enter Account Number:"))
           if acc_no in accounts:
             print("Account already exists!")
           else :
              name=input("Enter Account Holder Name:")
              balance=float(input("Enter initial deposit:"))
              accounts[acc_no]={"Name": name, "Balance": balance} 
              print("Account created successfully!")
    elif choice==2:
         acc_no=int(input("Enter Account Number:"))
         if acc_no in accounts:
             print("\n Account Holder:",accounts[acc_no]["Name"])
             print("Current Balance=Rs.",accounts[acc_no]["Balance"])
         else:
             print("Account Not Found!")
    elif choice==3:
        print("Thank you for using Bank Management System")
        break
    else :
         print("Invalid Choice!")
