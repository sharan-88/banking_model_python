class AccountRepository:
    #Class attribute to store all the elements
    account  = []
    account_counter = 1000
    # 1. class-level access: classmethod can access and modify the class-level attributes
    # 2. Differences
    # a. class method takes cls as its first argument
    # b. Instance.regular method takes self as its first argument
    # c. static method takes neither cls nor self as its first argument

    #Method to generate a new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter
    
    #Method to save Account
    @classmethod
    def save_account(cls, account):
        cls.account.append(account) 
    
    #Method to get all account
    def get_all_accounts(self):
        return self.account
    
    @classmethod 
    def get_account_by_id(cls, account_number):
        for account in cls.account:
             if account.account_number == account_number:
                 return account
        return 
    
    @classmethod
    def get_all_accounts(cls):
        return cls.account
    

    @classmethod 
    def get_accounts_by_type(cls,accountType):
        return[account for account in cls.account  if account.account_type == accountType]
    

    @classmethod
    def edit_account(cls,account_number):
        for each_account in cls.account:
            if each_account.account_number == account_number:
                pin_number =int(input("enter pin number \n"))
                if(pin_number == each_account.pin_number):
                    return each_account
                else:
                    print("InvalidPinException")
            else :
                print("no account exist with account number {accoun_number}")
                
            
            

