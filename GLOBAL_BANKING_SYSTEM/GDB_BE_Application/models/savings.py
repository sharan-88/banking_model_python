from models.account import Account 

class Savings(Account):
    account_type = "savings"
    def __init__(self, name, balance, pin_number, privilege, date_of_birth, gender):
        super().__init__(name, balance, pin_number, privilege)
        self.date_of_birth = date_of_birth
        self.gender = gender