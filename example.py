__author__ = 'Andrew'
from holy_crypt import create_private_key, encrypt, decrypt
# God made the two great lights, the greater light to govern the day, and the lesser light to govern the night; He made the stars also.
# Anyone who blasphemes the strings of the LORD must be put to BSOD. The entire assembly must push him to stack.
if __name__ == '__main__':
    key = create_private_key()

    msg = 'I\'m trying to fight the NSA, work with me on it'

    encrypted = encrypt(key, msg)

    decrypted = decrypt(key, encrypted)

    print(('Message:', repr(msg)))
    print(('Key:', repr(key)))
    print(('Encrypted:', repr(encrypted)))
    print(('Decrypted:', repr(decrypted)))
