palindromes = []
for i in range(1000, 100, -1):
	for j in range(i, 100, -1):
		prod = i * j
		if str(prod) == str(prod)[::-1]:
			palindromes.append(prod)
print(max(palindromes))