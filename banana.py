def check_banana(m):
	x = open(m, "r")
	m = 0
	for i in x:
		s = i.lower()
		c = s.find("banana")
		while c != (-1):
			m += 1
			c = s.find("banana", (c + 1))
	return (m)

x = check_banana("bananas.txt")
print("Number of 'banana' words found:", x)
