"""
use datetime module
"""
import datetime 
n = datetime.date.today()
d1 = n.strftime("%d-%b-%Y")

# txns_file_name = "%s_txns.txt" % account_num
# bal_file_name = "%s_bal.txt" % account_num
        
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

    def print_welcome(self):
        print("welcome ", self.name)
        print("your account is general type")
            
    def read_balance(self):
        balance_read = 0
        try:
            with open (self.bal_file_name,"r") as f:
                balance_read = f.read()
        except:
            pass
        return int(balance_read)
    
    def print_balance(self):
        print("Balance: ",self.balance)

    def deposit_balance(self, amount):
        self.balance  = amount + self.balance
        self.write_txn_to_file("{0:20} Deposit {1:15} €\n".format(d1,amount))
        self.write_balance()
        
    def withdraw_balance(self,withdraw):
        if withdraw <= self.balance:   
            self.balance = self.balance - withdraw
            self.write_txn_to_file("{0:20} Withdraw {1:15} €\n".format(d1,withdraw))
            self.write_balance()
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
    
    # def print_bank_detail(self):
    #     print(f"{self.name:20} {self.email:30} {self.account_num:15}",self.password)

    def bank_detail(self):
        return self.name+","+self.email+","+str(self.account_num)+","+self.credit_type+","+self.password+",\n"

        
        
class CreditAccount(Account):
    def __init__(self,name,email,account_num,credit_type,password):
        super().__init__(name,email,account_num,credit_type,password)

    def print_welcome(self):
        print("welcome ", self.name)
        print("your account is credit type")

    def withdraw_balance(self, withdraw):
        self.balance = self.balance - withdraw
        self.write_txn_to_file("{0:20} Withdraw {1:15} €\n".format(d1,withdraw))
        self.write_balance()