import math

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

def quickSort(a):
	def helper(b, l, r):
		if len(b[l:r]) == 0:
			return

		## Uncomment below for different pivot options (Default is first element)##

		## Last element pivot ##
		#a[l], a[r-1] = a[r-1], a[l]
	
		## Median element pivot ##
		#m = l+len(b[l:r])/2 if len(b[l:r]) % 2 != 0 else l-1+len(b[l:r])/2
		#if b[m] != min(b[l], b[m], b[r-1]) and b[m] != max(b[l], b[m], b[r-1]):
		#	b[l], b[m] = b[m], b[l]
		#elif b[r-1] != min(b[l], b[m], b[r-1]) and b[r-1] != max(b[l], b[m], b[r-1]):
		#	b[l], b[r-1] = b[r-1], b[l]

		pivot = b[l]
		i = l+1
		for j in range(l+1, r):
			if b[j] < pivot:
				b[j], b[i] = b[i], b[j]
				i += 1
		b[l], b[i-1] = b[i-1], b[l]

		helper(b, l, i-1)
		helper(b, i, r)

	helper(a, 0, len(a))

def quickSortWithComparisons(a):
	def helper(b, l, r):
		if len(b[l:r]) == 0:
			return 0

		total_comparisons = len(b[l:r])-1

		## Uncomment below for different pivot options (Default is first element)##

		## Last element pivot ##
		#a[l], a[r-1] = a[r-1], a[l]
	
		## Median element pivot ##
		#m = l+len(b[l:r])/2 if len(b[l:r]) % 2 != 0 else l-1+len(b[l:r])/2
		#if b[m] != min(b[l], b[m], b[r-1]) and b[m] != max(b[l], b[m], b[r-1]):
		#	b[l], b[m] = b[m], b[l]
		#elif b[r-1] != min(b[l], b[m], b[r-1]) and b[r-1] != max(b[l], b[m], b[r-1]):
		#	b[l], b[r-1] = b[r-1], b[l]
	
		pivot = b[l]
		i = l+1
		for j in range(l+1, r):
			if b[j] < pivot:
				b[j], b[i] = b[i], b[j]
				i += 1
		b[l], b[i-1] = b[i-1], b[l]

		total_comparisons += helper(b, l, i-1)
		total_comparisons += helper(b, i, r)
	
		return total_comparisons

	return helper(a, 0, len(a))
