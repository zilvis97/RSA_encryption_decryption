from prime_test import *

# generate a random prime number
def GenerateRandomPrime(min_val, num_of_witness, size = 32):
	big_number = pow(2, size)
	val = random.randint(min_val, big_number)
	while RabinMillerPrimalityTest(val, num_of_witness) == False:
		val = random.randint(min_val, big_number)

	return val