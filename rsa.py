#Learning how RSA encryption works
#basic demonstration of encryption/decryption

from fractions import gcd
import random

primes = [18966162103181877137104002000766961367217593615563,
          68527737995994650959675943774385180922666948136813,
          30281242611165201445430702074791135258029928737927,
          45406516671300548333311814388168688603381985062613,
          97038736927236393600823373710502730009860820708979,
          35963516379667279099632691498218709389825006221563,
          39074083144091764365782913889746140369634051774269,
          87829406556868104208432501228923251337658475933903]
          
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

def str_to_list(text):
    chars = []
    for letter in text:
        chars.append( ord(letter) )
    return chars

def list_to_str(chars):
    text = ""
    for char in chars:
        try:
            text += chr(int(char))
        except OverflowError:
            pass
    return text
############encryption stuff###########
def encrypt(num, pub_key1, pub_key2):
    return pow(num, pub_key1, pub_key2) #same as num**k1 % k2

def decrypt(num, priv_key, pub_key2):
    return pow(num, priv_key, pub_key2)

###generate keys###
p = random.choice(primes)
q = random.choice(primes)

n = p*q #n is multiple of 2 large primes
tn = (p-1)*(q-1)

e = coprime(tn)
d = modinv( e , tn )

print("Public Keys:",e,",",n)
print("Private key d:",d)
#private: d, p, q, tn

message = input("\nMessage:")

encrypted = []
for i in str_to_list(message):
    encrypted.append(encrypt(i, e, n))
print("Encrypted Message:",encrypted)

pk = int(input("\nEnter private key (d):"))
decrypted = []
for i in encrypted:
    decrypted.append(decrypt(i, pk, n))
print("\nDecrypted Message:",list_to_str(decrypted))
