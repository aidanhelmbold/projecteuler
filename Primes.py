def isPrime(inNum, list_primes):

	if inNum in list_primes: return True

	for i in list_primes:
		if inNum % i == 0: 
			print str(i) + " - " + str(inNum % i)
			return False

	for j in range(int(max(primes)), int(inNum  / 2), 2):
		if inNum % j == 0: 
			print str(j) + " - " + str(inNum % j)
			return False

	list_primes.append(inNum)
	print(list_primes)
	return True


primes = [2, 3]

for i in range(3,20):
	print str(i) + str(isPrime(i, primes))



