def mergeSort(a):
	if len(a) == 0 or len(a) == 1:
		return a

	sorted = []
	h1 = mergeSort(a[:len(a)//2])
	h2 = mergeSort(a[len(a)//2:])
	i = j = 0
	for k in range(len(a)):
		if i == len(h1) or j == len(h2):
			sorted += h1[i:] + h2[j:]
			break

		if h1[i] < h2[j]:
			sorted.append(h1[i])
			i += 1
		else:
			sorted.append(h2[j])
			j += 1
	return sorted
