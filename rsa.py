#Learning how RSA encryption works
#basic demonstration of encryption/decryption

from conv import *
from fractions import gcd
import random

primes = [18966162103181877137104002000766961367217593615563,
          68527737995994650959675943774385180922666948136813,
          30281242611165201445430702074791135258029928737927,
          45406516671300548333311814388168688603381985062613,
          97038736927236393600823373710502730009860820708979,
          35963516379667279099632691498218709389825006221563,
          39074083144091764365782913889746140369634051774269,
          87829406556868104208432501228923251337658475933903,
          99701007192486571157506448414512864891510440378097,
          22562323080364605847165435922793394781582610307019,
          72166658850906333926882447749629659951480345596937]
          
#egcd() and modinv() courtesy of stackoverflow
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    """x = modinv( a , m ) --> (x * a) % m = 1"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def coprime(num):
    """returns the lowest number with no common factors to num"""
    for co in range(13, num):
        if gcd(co,tn) == 1:
            return co

############encryption stuff###########
def encrypt(num, pub_key1, pub_key2):
    return pow(num, pub_key1, pub_key2) #same as num**k1 % k2

def decrypt(num, priv_key, pub_key2):
    return pow(num, priv_key, pub_key2)

###generate keys###
p = 21347#random.choice(primes)
q = 24593#random.choice(primes)

n = p*q #n is multiple of 2 large primes
tn = (p-1)*(q-1)

e = 65537#coprime(tn)
d = modinv( e , tn )

#private: d, p, q, tn
#public: e, n

#public
print("Alice wants to send a message to Bob")
print("\nPublicly transmitted from Bob to Alice:")
print("Public Keys:",e,",",n)

#sender
print("\nPrivate on Bob's machine:")

message = input("Message:")

number_msg = s2n(message)
print("Encrypting:",number_msg)
encrypted = encrypt(number_msg, e, n)

#public again
print("\nBob's public tranmission to Alice")
print("Encrypted Message:",encrypted)

print("\nEve attempts to read message:")
pk = int(input("Enter private key (hint, you can't, but you can try):"))
decrypted = decrypt(encrypted, pk, n)
print("Eve's Decrypted Message:",n2s(decrypted))

#receiver
print("\nPrivate on Alice's machine")
print("Private key d:",d)
pk = int(input("Enter private key (d):"))
decrypted = decrypt(encrypted, pk, n)
print("Alice's Decrypted Message:",n2s(decrypted))
