def fib4(n):
	a, b = 0, 1
	while a < n:
		print(a, end=‘ ’)
		a, b = b, a+b
	print()
fib4(1000)