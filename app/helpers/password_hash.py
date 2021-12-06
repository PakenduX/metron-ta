from argon2 import PasswordHasher

hasher = PasswordHasher()


def hash_password(password):
    return hasher.hash(password)


def verify_password(hash, password):
    return hasher.verify(hash, password)
