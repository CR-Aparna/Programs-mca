class BankAccount:
	def __init__(self,account_number,name,account_type,balance=0.0):
		self.account_number = account_number
		self.name = name
		self.account_type = account_type
		self.balance = balance
	def deposit(self,amount):
		if amount>0:
			self.balance += amount
			print"Deposited{0}.New Balance:{1}".format(amount,self.balance)
		else:
			print"Deposit amount must be positive."
	def withdraw(self,amount):
		if amount>0:
			if self.balance >= amount:
				self.balance -= amount
				print"Withdrew {0}.New balance{1}".format(amount,self.balance)
			else:
				print"Insufficient balance for withdrawal."
		else:
			print"Withdrawal amount must be positive."

	def get_balance(self):
		return self.balance
	def account_details(self):
		return "Account Number:{0}\n Name:{1}\n Account Type:{2}\n Balance:{3}".format(self.account_number,self.name,self.account_type,self.balance)
 
account1 = BankAccount(account_number = "123456789",name = "John Doe",account_type = "Checking",balance = 1000.0)

print account1.account_details()
account1.deposit(500)
account1.withdraw(300)
print"Updated Balance:",account1.get_balance()


