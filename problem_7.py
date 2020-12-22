primes = [2]
biggest_val = 1
while len(primes) < 10001:
	biggest_val += 2

	prime = True
	for i in primes:
		if biggest_val % i == 0:
			prime = False

	if prime == True:
		primes.append(biggest_val)
		print(f'{len(primes)}: {biggest_val}')
	
print(max(primes))