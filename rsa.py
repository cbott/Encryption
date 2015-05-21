#Learning how RSA encryption works
#basic demonstration of encryption/decryption

from fractions import gcd
import random

primes = [52225826216283694472093, 64695235256140913657017,
          36297494658228210202973, 31155565732826674528429,
          64156422650326195323241, 9491097298620527384257,
          89595162380538365029307, 26642104611992532346009]

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
p = random.choice(primes)
q = random.choice(primes)

n = p*q #n is multiple of 2 large primes
tn = (p-1)*(q-1)

e = coprime(tn)
d = modinv( e , tn )

print("Public Keys:",e,",",n)
print("Private key d:",d)
#private: d, p, q, tn

message = 1234
print("\nMessage:",message)

encrypted = pow(message, e, n) #same as message**e % n
print("Encrypted Message:",encrypted)

#pk = int(input("Enter private key (d):"))
decrypted = pow(encrypted, d, n)
print("Decrypted Message:",decrypted)
