from cryptography.fernet import Fernet

class Cryptography:
    
    key = None

    @classmethod
    def generateKey(cls):
        cls.key = Fernet.generate_key()

    @classmethod
    def getKey(cls):
        return cls.key
    
    @classmethod
    def destroyKey(cls):
        cls.key=None
    
    @classmethod
    def encrypt(cls,string):
        string_bytes = bytes(string,'utf-8')
        return Fernet(cls.key).encrypt(string_bytes)

    @classmethod
    def decrypt(cls,string_byte):
        string = Fernet(cls.key).decrypt(string_byte).decode()
        return string
