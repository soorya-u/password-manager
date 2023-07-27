import hashlib

def verifyingHash(username,password):
    stored_username_hash=None
    stored_password_hash=None
    username_hash=hashlib.sha512(username.encode()).hexdigest()
    password_hash=hashlib.sha512(password.encode()).hexdigest()
    if(username_hash==stored_username_hash and password_hash==stored_password_hash):
        return True
    return False    