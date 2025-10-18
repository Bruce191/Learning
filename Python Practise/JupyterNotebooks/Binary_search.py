



def binary_search(mylist, target):

	#first step is getting the indexes of the first and last value
	low, high = 0, len(mylist) - 1

    #ensuring there is always something to search
	while low <= high:

		#we dont do mid = (len array) //2 because we are splitting the list each time with high low,
		#so we need to track high,low as they define our new list each time
		mid = (low + high) // 2

		if mylist[mid] == target:
			return mid
		elif mylist[mid] < target:
			#if mid is smaller tha the target then the beginning of our new list is mid + 1 (second side of list)
			low = mid + 1
		else:
			high = mid - 1


mylist = [ 2, 3, 7, 7, 11, 15, 25]
target = 25

print(binary_search(mylist, target))