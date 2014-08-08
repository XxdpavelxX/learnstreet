def binary_search(list, item):
	low = 0
	high = len(list)-1
	x=0   #number of tries it took to find number
	
	while low <= high:
		mid = (low + high)/2
		guess = list[mid]
		
		if guess == item:
			print "Found in %s tries" %x
			return mid
			
			
		if guess >= item:
			high = mid - 1
			x=x+1
			
		else:
			low = mid+1
			x=x+1
			
	return None
