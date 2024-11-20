from models.privileges import Privilege

class AccountPrivilegesManager:
    
    privileges = {
        'PREMIUM' : 100000,
        'GOLD' : 50000,
        'SILVER' : 25000
    }
    
    @classmethod
    def get_transfer_limit(cls, privilege):
        return cls.privileges.get(privilege, 0)# if privillage is not found it returns 0 by default