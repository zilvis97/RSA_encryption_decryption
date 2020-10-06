import random

#Returns TRUE if candidate is deemed to be prime, FALSE otherwise
def RabinMillerPrimalityTest(candidate, num_of_witness):
	if candidate == 2:
		return True
	if candidate % 2 == 0:
		return False

	k = 0
	q = candidate - 1

	while q % 2 == 0:
		k += 1
		q //= 2

	found = False
	for _ in range(num_of_witness):
		a = random.randrange(2, candidate - 1)	# new 'a' for every witness
		res = pow(a, q, candidate)
		if res == 1 or res == candidate - 1:
			found = True
			continue
		for j in range(k-1):
			deg = pow(2, j) * q
			res = pow(a, deg, candidate)
			if res == candidate - 1:
				found = True
				break

	return found