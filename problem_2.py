def next_fibonacci(a, b):
	return a+b

def even_fib_less_than(N):
	fib_list = [1, 2]
	answer = 2
	while fib_list[-1] < N:
		fib_list.append(next_fibonacci(fib_list[-2], fib_list[-1]))
		if fib_list[-1]%2==0:
			answer += fib_list[-1]

	return answer

print(even_fib_less_than(4000000))
