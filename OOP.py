class BankCard:
    def __init__(self, owner, number, provider):
        self.owner=owner
        self.number=number
        self.provider=provider

    def get_owner(self):
            print(self.owner)
    def get_number(self):
            print(self.number)
    def get_provider(self):
            print(self.provider)

bank_card = BankCard('Jan Kowalski', '9', 'MasterCard')
bank_card.get_owner()
bank_card.get_number()
bank_card.get_provider()
print("\n")

class BankAccount:
    def __init__(self, owner, balance, bank):
        self.owner=owner
        self.balance=balance
        self.bank=bank

    def get_owner(self):
            print(self.owner)
    def get_balance(self):
            print(self.balance)
    def get_bank(self):
            print(self.bank)
    def set_balance(self):
            print(input(self.balance))

bank_account = BankAccount('Jan Kowalski', '1000', 'Pekao')
bank_account.get_owner()
bank_account.get_balance()
bank_account.get_bank()
bank_account.set_balance()
print("\n")

class Bank:
    def __init__(self,name,bank_accounts,bank_cards):
        self.name=name
        self.bank_accounts=bank_accounts
        self.bank_cards=bank_cards

    def get_name(self):
             print(self.name)
    def get_bank_accounts(self):
             print(self.bank_accounts)
    def get_bank_cards(self):
             print(self.bank_cards)

Bank_ = Bank('Norbert','Pekao, Mbank, Pko','3')
#Bank_.get_name()
Bank_.get_bank_accounts()
Bank_.get_bank_cards()
print("\n")

class CreditCard(BankCard):
    def __init__(self, owner, number, provider, balance, payments_history):
        super().__init__(owner, number, provider)
        self.balance = balance
        self.payments_history = payments_history 
    
    def get_balance(self):
            print(self.balance)
    def get_payments_history(self):
            print(self.payments_history)
Credit_Card=CreditCard('Jan Kowalski', '9', 'MasterCard','25k','-100,+250,-150...')
#bank_card.get_owner()
#bank_card.get_number()
#bank_card.get_provider()
Credit_Card.get_balance()
Credit_Card.get_payments_history()
print("\n")

class GoldenCreditCard(CreditCard):
    def __init__(self, owner, number, provider, balance, payments_history, reward_points):
        super().__init__(owner, number, provider, balance, payments_history,)
        self.reward_points= reward_points
    def get_reward_points(self):
            print(self.reward_points)
Golden_CreditCard=GoldenCreditCard('Jan Kowalski', '9', 'MasterCard','25k','-100,+250,-150...','150 points')
Golden_CreditCard.get_reward_points()
print("\n")

class PremiumBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, financial_manager):
        super().__init__(owner, balance, bank)
        self.financial_manager=financial_manager
    def get_financial_manager(self):
            print(self.financial_manager)
PremiumBankAccount1=PremiumBankAccount('Jan Kowalski', '1000', 'Pekao','Andrzej Duda')
PremiumBankAccount1.get_financial_manager()
print("\n")

class StudentBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, overdraft_balance, overdraft_limit):
        super().__init__(owner, balance, bank)
        self.overdraft_balance=overdraft_balance
        self.overdraft_limit=overdraft_limit
    def get_overdraft_balance(self):
            print(self.overdraft_balance)
    def get_overdraft_limit(self):
            print(self.overdraft_limit)
StudentBankAccount1=StudentBankAccount('Jan Kowalski', '1000', 'Pekao',"10,000,000","50,000,000")
StudentBankAccount1.get_overdraft_balance()
StudentBankAccount1.get_overdraft_limit()







            
        
    
       