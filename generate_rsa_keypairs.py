import random

#find gcd of 2 numbers
def gcd(a, b):
	while a != 0:
		a, b = b % a, a
	return b

def findInverseMod(a, b):
	if gcd(a, b) != 1:
		return None

	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, b

	while v3 != 0:
		q = u3 // v3
		v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
	return u1 % b


#generate public and private key pairs
def GenerateRSAKeyPair(prime1, prime2):
	n = prime1 * prime2
	fn = (prime1 - 1) * (prime2 - 1)

	#generate e that is relatively prime to prime1-1 and prime2-1
	while True:
		e = random.randrange(2, fn)
		if gcd(fn, e) == 1:
			break

	d = findInverseMod(e, fn)

	public_key = (e, n)
	private_key = (d, n)

	return (public_key, private_key)