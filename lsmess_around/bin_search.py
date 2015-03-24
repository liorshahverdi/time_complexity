def binarySearch(a, key, imin, imax):
	while imax >= imin:
		imid = int((imin + imax) / 2)
		if a[imid] == key:
			return imid
		elif a[imid] < key:
			imin = imid+1
		else:
			imax = imid - 1
	return -1

list = [2,3,4,5,6,8,10]
k = 10
print binarySearch(list,k, 1,7)