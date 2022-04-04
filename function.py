
import datetime 
n = datetime.date.today()
d1 = n.strftime("%d-%b-%Y")
 

class Account:
    def __init__ (self,name,email,account_num,credit_type,password):
        self.name = name
        self.email = email
        self.account_num = account_num
        self.credit_type = credit_type
        self.password = password
        self.txns_file_name = "%s_txns.txt" % self.account_num
        self.bal_file_name = "%s_bal.txt" % self.account_num
        self.balance = self.read_balance()

    def read_balance(self):
        with open (self.bal_file_name,"r") as f:
            balance_read = f.read()
            try:
                return int(balance_read)
            except:
                return 0
    
    def print_balance(self):
        print("Balance: ",self.balance)

    def deposit_balance(self, amount):
        self.balance  = amount + self.balance
        self.write_txn_to_file("{0:20} Deposit {1:15} €\n".format(d1,amount))
        self.write_balance()
        
    def withdraw_balance(self,withdraw):
        #  self.balance  = self.balance - withdraw
        #  self.write_txn_to_file("withdraw: "+str(withdraw)+"$"+"\n")
        #  self.write_balance()
        if withdraw <= self.balance:   
            self.balance = self.balance - withdraw
            self.write_txn_to_file("{0:20} Withdraw {1:15} €\n".format(d1,withdraw))
            
        else:
            print("check the amount")
 
    def write_txn_to_file(self, txn_text):
        with open (self.txns_file_name,"a") as f:
            f.write(txn_text)

    def read_txt_file(self):
        with open(self.txns_file_name,"r") as f:
            read_txt = f.read()
            return read_txt
    
    def print_txt(self):
        print(self.read_txt_file())
   
    def write_balance(self):
        with open(self.bal_file_name,"w") as f:
            f.write(str(self.balance))
    
    def print_bank_detail(self):
        print(f"{self.name:20} {self.email:30} {self.account_num:15}",self.password)

    def bank_detail(self):
        return self.name+","+self.email+","+str(self.account_num)+","+self.credit_type+","+self.password+"\n"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
    if credit_type == "YES":
        print("your account is credit type")
    else:
        pass
    while True:
        password = input("password:")
        if len(password) >= 8:
            print("password saved")
            break
        else:
            print("password is too short.\nminimum is 8 characters")
    #balance = self.balance
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
                print("welcome")
                user_account = account
                break
            else:
                print("wrong password,enter the correct password")
                break
    else:
        print("account number doesnot exit")


while bank_menu != '5':
    bank_menu = input("************************\n1:CHECK BALANCE\n2:DEPOSIT AMOUNT\n3:WITHDRAW AMOUNT\n4:TRANSFER DETAILS\n5:Ewxit\nEnter an option:")
    if bank_menu == "1":
        user_account.print_balance()
    if bank_menu == "2":
        deposit_amount = int(input("enter the amount to deposit:"))
        user_account.deposit_balance(deposit_amount)
        user_account.print_balance()
    if bank_menu == "3":
        withdraw_amount = int(input("enter the  amount to withdraw:"))
        user_account.withdraw_balance(withdraw_amount)
        user_account.print_balance()
    if bank_menu == "4":
        user_account.print_txt()