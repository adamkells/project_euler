def smallest_factor(factor, N):
	for i in range(max(2, factor), N+1):
		if N%i==0:
			return int(i)


factors = [1]
N = 600851475143

while N>1:
	factors.append(smallest_factor(max(factors), N))
	N = int(N/factors[-1])
	print(N)
print(factors)