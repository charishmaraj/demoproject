from account import *
import secrets
hexstr = secrets.token_hex(4)
id1 =int(hexstr,16)

## TODO only numeric 8 digit

l = []
choose_option = ''
bank_menu = '' 




with open("account_detail.txt","r") as f:
    for file in f:
        s = file.split(",")
        if(len(s)) >= 4:
            if s[3] == "YES":
                b1 = CreditAccount(s[0],s[1],s[2],s[3],s[4])
            else:
                b1 = Account(s[0],s[1],s[2],s[3],s[4])
            l.append(b1)

choose_option = input("1:CREATE ACCOUNT\n2:LOGIN\nChoose your option: ")
if choose_option == "1":
    name = input("name:")
    email = input("email_id:")
    account_num = id1
    print("your bankaccount number: ",id1)
    print("would you like to take 'Credit Account Type': YES OR NO ")
    credit_type = input("")
    while True:
        password = input("password:")
        if len(password) >= 8:
            print("password saved")
            break
        else:
            print("password is too short.\nminimum is 8 characters")
    #balance = self.balance
    if credit_type.upper() == "YES":
        print("your account is credit type")
        b = CreditAccount(name,email,account_num,credit_type,password)
    else:
        b = Account(name,email,account_num,credit_type,password)
    l.append(b)

    with open("account_detail.txt","w") as f:
        for detail in l:
            data = detail.bank_detail()
            f.write(data)

if choose_option == "2":
    account_id = input("enter account_number: ")
    # password_check = input("enter password:")
    user_account = None

    for account in l:
        i1 = account.account_num
        # i2 = account.password
        if account_id == i1:
            password_check = input("enter password:")
            i2 = account.password
            if password_check == i2:
                user_account = account
                user_account.print_welcome()
                break
            else:
                print("wrong password,enter the correct password")
                break
    else:
        print("account number doesnot exit")


while bank_menu != '5':
    bank_menu = input("************************\n1:CHECK BALANCE\n2:DEPOSIT AMOUNT\n3:WITHDRAW AMOUNT\n4:TRANSFER DETAILS\n5:Exit\nEnter an option:")
    if bank_menu == "1":
        user_account.print_balance()
    if bank_menu == "2":
        deposit_amount = int(input("enter the amount to deposit:"))
        user_account.deposit_balance(deposit_amount)
        user_account.print_balance()
    if bank_menu == "3":
        withdraw_amount = int(input("enter the  amount to withdraw:"))
        user_account.withdraw_balance(withdraw_amount)
        # if user_account.credit_type == "YES":   
            # user_account.withdraw(withdraw_amount)              
        user_account.print_balance()
    if bank_menu == "4":
        user_account.print_txt()
        


    


