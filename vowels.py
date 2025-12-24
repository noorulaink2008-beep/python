text = input("Enter a string")
vowels = 0
for ch in text:
	if ch in "adacscsc":
		vowels += 1
	print("Total vowels =", vowels)