import os   # This module use for create and delete the file in location
import pickle  # This module use for getting the user data dump to another file and again getting the same data and secure purpose
import pathlib  #This module use for create file path

class Bank_system():

    def CreateAccount(self):
        try:
              self.Acct_NO = int(input("Enter the Acct Number:"))
              self.Holder_Name = input("Enter the customer Name:")
              self.date_of_Birth = input("Enter the Birth Date(dd/mm/yyyy):")
              self.Address = input("Enter the Address:")
              self.Phone_Number = int(input("Enter the Phone Number:"))
              self.type = input("Ente the type of account [C/S] : ")
              self.Deposit_Amt = int(input("Enter the amount of doposit:"))
              print("Account Created")
        except ValueError:
              print("Invalid value,Please check")


    def Account(self):

         try:
             obj = Bank_system()
             obj.CreateAccount()
             file = pathlib.Path("accounts.data")
             if file.exists():
                infile = open('accounts.data', 'rb')
                oldlist = pickle.load(infile)
                oldlist.append(obj)
                infile.close()
                os.remove('accounts.data')
             else:
                oldlist = [obj]
             outfile = open('newaccounts.data', 'wb')
             pickle.dump(oldlist, outfile)
             outfile.close()
             os.rename('newaccounts.data', 'accounts.data')
         except FileNotFoundError:
             print("File has no records")

    def ViewAll(self):
         try:
             file = pathlib.Path("accounts.data")
             if file.exists():
                infile = open('accounts.data', 'rb')
                mylist = pickle.load(infile)
                for item in mylist:
                    print(item.Acct_NO,'//', item.Holder_Name,'//', item.date_of_Birth,'//', item.Address,'//',item.Phone_Number,'//',item.type ,'//',item.Deposit_Amt)
                    infile.close()
             else:
                print("No records to display")
         except FileNotFoundError:
             print("File Doesn't exist ")

    def search(self):
         try:
             file = pathlib.Path("accounts.data")
             if file.exists():
                infile = open('accounts.data', 'rb')
                mylist = pickle.load(infile)
                infile.close()
                found = False
                NO = int(input("\tEnter The account No. : "))
                for item in mylist:
                    if item.Acct_NO == NO:
                       print("Holder Name is :",item.Holder_Name)
                       print("Holder birth Dats is:",item.date_of_Birth)
                       print("Address detail:",item.Address)
                       print("Account type is :",item.type)
                       print("Phone Number is :",item.Phone_Number)
                       print("Your account Balance is = ", item.Deposit_Amt)
                       found = True
             else:
                 print("No records to Search")
             if not found:
                  print("No existing record with this number")

         except FileNotFoundError:
                print("No records to Search")
         except ValueError or UnboundLocalError:
                print("Invalid value entered, Please Check")

    def BalanceDeposit(self):
         try:
              file = pathlib.Path("accounts.data")
              if file.exists():
                 infile = open('accounts.data', 'rb')
                 mylist = pickle.load(infile)
                 infile.close()
                 os.remove('accounts.data')
                 NO = int(input("\tEnter The account No. : "))
                 for item in mylist:
                    if item.Acct_NO == NO:
                        amount = int(input("Enter the amount to deposit : "))
                        item.Deposit_Amt += amount
                        print("Deposit Completed")
                        print("your current balance is>>>>",item.Deposit_Amt)
              else:
                  print("No records to Search")
              outfile = open('newaccounts.data', 'wb')
              pickle.dump(mylist, outfile)
              outfile.close()
              os.rename('newaccounts.data', 'accounts.data')
         except ValueError:
             print("invalid value entered,Please check it")
         except FileNotFoundError:
             print("File Not Found")

    def BalanceWithdraw(self):
         try:
             file = pathlib.Path("accounts.data")
             if file.exists():
                 infile = open('accounts.data', 'rb')
                 mylist = pickle.load(infile)
                 infile.close()
                 os.remove('accounts.data')
                 NO = int(input("\tEnter The account No. : "))
                 for item in mylist:
                    if item.Acct_NO == NO:
                        amount = int(input("Enter the amount to withdraw : "))
                        if amount <= item.Deposit_Amt:
                            item.Deposit_Amt -= amount
                            print("Withdraw completed")
                            print("Your current balance is >>>",item.Deposit_Amt)
                        else:
                            print("You cannot withdraw larger amount")

             else:
                 print("No records to Search")
             outfile = open('newaccounts.data', 'wb')
             pickle.dump(mylist, outfile)
             outfile.close()
             os.rename('newaccounts.data', 'accounts.data')
         except ValueError:
             print("invalid value entered,Please check it")
         except FileNotFoundError:
             print("File Not Found")

    def deleteAccount(self):
         try:
             file = pathlib.Path("accounts.data")
             if file.exists():
                infile = open('accounts.data', 'rb')
                oldlist = pickle.load(infile)
                infile.close()
                newlist = []
                NO = int(input("\tEnter The account No. : "))
                for item in oldlist:
                    if item.Acct_NO != NO:
                       newlist.append(item)
                       print("Account Removed")
                    os.remove('accounts.data')
                    outfile = open('newaccounts.data', 'wb')
                    pickle.dump(newlist, outfile)
                    outfile.close()
                    os.rename('newaccounts.data', 'accounts.data')
                    print("Account Deleted")
         except FileNotFoundError:
              print("File Not Found")

####-----update the user acctount-------#######
    def modifyAccount(Self):
        try:
           file = pathlib.Path("accounts.data")
           if file.exists():
                infile = open('accounts.data', 'rb')
                oldlist = pickle.load(infile)
                infile.close()
                os.remove('accounts.data')
                NO = int(input("\tEnter The account No. : "))
                for item in oldlist:
                    if item.Acct_NO == NO:
                       item.Holder_Name = item.Holder_Name
                       item.date_of_Birth = item.date_of_Birth
                       item.Address = input("Enter the Address Detail: ")
                       item.Phone_Number = int(input("Enter the Phone Number : "))
                       item.type = input("Ente the type of account [C/S] : ")
                       item.Deposit_Amt = item.Deposit_Amt
                       print("Your Account updated")
                outfile = open('newaccounts.data', 'wb')
                pickle.dump(oldlist, outfile)
                outfile.close()
                os.rename('newaccounts.data', 'accounts.data')
        except ValueError:
             print("invalid value entered,Please check it")
        except FileNotFoundError:
             print("File Not Found")





###--------this statement calling the whole class---------####
obj = Bank_system() # create the instance class




####___________This intro section of project-----------######
ch = ''
num = 0
#intro()

while ch != 8:
    # system("cls");
    print("\t\t\t\t\t\t\t\t\************WELCOME TO MY BANK**************\t\t\t\t\t\t\t\t\t")
    print("HOW CAN I HELP YOU")
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. BALANCE DEPPOSIT ")
    print("\t3. BALANCE WITHDRAW ")
    print("\t4. ACCOUNT SEARCH")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. DELETE ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. Exit")
    print("\tSelect Your Option (1-8) ")

    ch = input("Enter your choice : ")

    if ch == '1':
        obj.Account()
    elif ch == '2':
        obj.BalanceDeposit()
    elif ch == '3':
        obj.BalanceWithdraw()
    elif ch == '4':
        obj.search()
    elif ch == '5':
        obj.ViewAll()
    elif ch == '6':
        obj.deleteAccount()
    elif ch == '7':
        obj.modifyAccount()
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else:
        print("Invalid choice")


