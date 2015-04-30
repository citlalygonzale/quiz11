import math
def readnum(m):
	a=open(c, "r")
	total = 0
	l = []
	x = 0
	y = 0
	s = 0
	for i in a:
		total = total + (int(i))
		l.append(int(i))
		value = len(l)
		average = total / value
		while (a < value):
			y = ((l[x]) - average) ** 2
			x = x + 1
			s = s + y
			standardev_ = math.sqrt(s / value)

	print("Number of values:", value)
	print("Total of values:", total)
	print("Average:", average)
	print("Standard Desviation:", standardev_)

readnum("random.txt")
