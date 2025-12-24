n = int(input("Enter a number"))
sum = 0
print("Numbers from 1 to", n, "are:", end=" ")
for i in range(1, n + 1):
	print(i, end=" ")
	sum += i
	print("The sum is", sum)