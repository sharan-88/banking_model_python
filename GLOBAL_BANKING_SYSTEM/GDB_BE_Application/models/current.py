from models.account import Account 

class Current(Account):
    account_type ="current"
    def __init__(self, name, balance, website_url, pin_number, privilege, registration_number):
        super().__init__( name, balance, pin_number, privilege)
        self.registration_number = registration_number
        self.website_url = website_url