#!/usr/bin/env python
'''
Created on 27 May 2016

@author: samuel.downton
'''

import  random
import fractions
from egcd import isprime, mulinv, mod_exp

min_prime = 1000000
max_prime = 1010000

primes = [i for i in range(min_prime,max_prime) if isprime(i)]

p = random.choice(primes)
q = random.choice(primes)

print "Prime numbers are ", p , q
'''z
 Generate a Modulus
'''
n = p * q 
print "n =", n

'''
Calculate "Totient" of n Totient is number of numbers less than n which are coprime with n.
Coprimes have only a common factor of 1
phi(n) = phi(q*p) = phi(q)*phi(p) = (p-1)(q-1) as for a prime, p, phi = p - 1
'''

phi_n = (p - 1) * (q - 1)
print "phi(n) = ", phi_n

'''
Pick a number with a greatest common divisor of 1 with Phi n
This is our PUBLIC key!
In reality 65537 usually used, but we will pick something smaller to speed things up.
'''

pub = 0
i = 2

while True:
    if fractions.gcd(i, phi_n) == 1:
        pub = i
        break
    i += 1
print "Public key is ", pub

# Find the number that is the inverse of the public key mod phi_n such that (public * x) mod phi_n = 1 

priv = mulinv(pub, phi_n)
print "Private key is ", priv

message = 42

print "Starting Message: ", message

# Encrypt
print ""
print "Encrypt with Public Key"
cipher = mod_exp(message, pub, n) # calculates (message ** pub) % n
print "Encrypted Message: ", cipher

print ""
print "Decrypt with Private Key"
original = mod_exp(cipher, priv, n) # calculates (cipher ** priv) % n
print "Decrypted Message: ", original

print ""
print "Encrypt with Private Key"
cipher = mod_exp(original, priv, n)
print "Encrypted Message: ", cipher

print""
print "Decrypt with Public Key"
original = mod_exp(cipher, pub, n)
print "Decrypted Message: ", original

# The key here is that to calculate Phi_n is very hard if you do not know p & q
# And calculating p and q is incredibly hard for massive numbers.
