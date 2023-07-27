import hashlib

def creatingHash(username,password):
    username_hash=hashlib.sha512(username.encode()).hexdigest()
    password_hash=hashlib.sha512(password.encode()).hexdigest()
    return {'usename_hash':username_hash,'password_hash':password_hash}