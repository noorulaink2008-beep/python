a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))


largest = a
if b > largest:
	largest = b
if c > largest:
	largest = c
print("Largest = ", largest)