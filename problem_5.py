i = 38
div = 0
while div == 0:
	i += 19
	counters = 0
	for j in range(1, 21):
		if i % j == 0:
			counters += 1
	if counters == 20:
		div = 1
print(i)