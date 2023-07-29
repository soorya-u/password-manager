import hashlib


class Hashing:

    # * Function to create Hash
    # * Parameters: Password
    # * Return Value: Hashed Password
    def creatingHash(password):
        password_hash = hashlib.sha512(password.encode()).hexdigest()
        return password_hash

    # * Function to verify Hash
    # * Parameters: Password, Stored Passowrd Hash
    # * Return Value: True or False
    def verifyingHash(password, stored_password_hash):
        password_hash = hashlib.sha512(password.encode()).hexdigest()
        if (password_hash == stored_password_hash):
            return True
        return False
