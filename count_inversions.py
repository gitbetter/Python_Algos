## Returns the inversion count of list a ##

def count(a):
	if len(a) == 1 or len(a) == 0:
		return 0

	b = a[:len(a)//2]
	c = a[len(a)//2:]

	x = sort_and_count(b)
	y = sort_and_count(c)
	
	i = j = inv_count = 0
	for k in range(len(a)):
		if i == len(b) or j == len(c):
			break
		if b[i] < c[j]:
			i += 1
			continue
		else:
			j += 1
			inv_count += len(b) - i

	return inv_count + x + y
	
## Sorts and returns inversion count of list a ##

def sort_and_count(a):
	if len(a) == 1 or len(a) == 0:
		return 0

	s = []

	b = a[:len(a)//2]
	c = a[len(a)//2:]

	x = sort_and_count(b)
	y = sort_and_count(c)
	
	i = j = inv_count = 0
	for k in range(len(a)):
		if i == len(b) or j == len(c):
			s += b[i:] + c[j:]
			break
		if b[i] < c[j]:
			s.append(b[i])
			i += 1
			continue
		else:
			s.append(c[j])
			j += 1
			inv_count += len(b) - i

	a[:] = s
	return inv_count + x + y
