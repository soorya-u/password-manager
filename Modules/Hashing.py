import hashlib
import random


class Hashing:

    # * Function to create Hash
    # * Parameters: Password
    # * Return Value: Hashed Password
    @classmethod
    def creatingHash(cls, password: str) -> str:
        password_hash = hashlib.sha512(password.encode()).hexdigest()
        return password_hash

    # * Function to verify Hash
    # * Parameters: Password, Stored Passowrd Hash
    # * Return Value: True or False
    @classmethod
    def verifyingHash(cls, password: str, stored_password_hash: str) -> bool:
        password_hash = hashlib.sha512(password.encode()).hexdigest()
        if (password_hash == stored_password_hash):
            return True
        return False

    def generatePassword():
        pass