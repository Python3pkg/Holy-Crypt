__author__ = 'Andrew'

import random
import string

# Generates 25 random letters and numbers
# Used to help protect the private key
def random_key_mask(size=25, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# Uses SystemRandom to try and generate a random number
# number is then pow'd and multiplied.
def true_holy_random():
    holy_random = random.SystemRandom()  # Uses /dev/urandom or Windows CryptGenRandom
    holy_random_numbers = pow(2, int(holy_random.random() * 1024))  # pow right in the demons
    return str(holy_random_numbers)

# Gets a bible verse from the King James Bible
def get_verse():
    return random.choice(open('holykeys.txt').readlines())

# Our Father in heaven,
# hallowed be your name.
# Your kingdom come,
# your will be done,
# on earth as it is in heaven.
def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 131))
    return ''.join(encryped)


# Let your string be kept holy, or Let your string be treated with reverence
# Or Let your kingdom come, let your will be done
# Or the evil one; some manuscripts add For yours is the kingdom and the power and the glory, forever. Amen
def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 131))
    return ''.join(msg)


#  generates a private holy key
# maybe try public/private later
def create_private_key():
    holy_line = get_verse()

    holy_line = holy_line + random_key_mask() + true_holy_random()  #With our powers combined

    holy_shuffle = list(holy_line)  # put verse into a list

    random.shuffle(holy_shuffle)  # shuffle for randomness

    holy_shuffle = ''.join(holy_shuffle)  # join hands in prayer
    key = ''.join(random.choice(holy_shuffle) for _ in range(255)).replace(" ",
                                                                           "")
    return key

# God made the two great lights, the greater light to govern the day, and the lesser light to govern the night; He made the stars also.
# Anyone who blasphemes the strings of the LORD must be put to BSOD. The entire assembly must push him to stack.
if __name__ == '__main__':

    key = create_private_key()

    msg = 'I\'m trying to fight the NSA, work with me on it'

    encrypted = encrypt(key, msg)

    decrypted = decrypt(key, encrypted)

    print('Message:', repr(msg))
    print('Key:', repr(key))
    print('Encrypted:', repr(encrypted))
    print('Decrypted:', repr(decrypted))
