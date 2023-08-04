import re

class Regex:

    @classmethod
    def verifyMasterUserName(cls,master_user_name):
        return bool(re.match('^[A-Za-z0-9._]+$', master_user_name))
    
    @classmethod
    def verifyPassword(cls,master_password):
        if len(master_password) >= 8 and len(master_password) <= 35:
            return True
        return False