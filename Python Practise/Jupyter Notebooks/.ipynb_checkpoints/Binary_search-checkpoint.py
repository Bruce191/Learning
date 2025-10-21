



def binary_search(mylist, target):
	#first step is getting the indexes of the first and last value
	low, high = 0, len(mylist) - 1
	result = -1

    #ensuring there is always something to search
	while low <= high:

		#we dont do mid = (len array) //2 because we are splitting the list each time with high low,
		#so we need to track high,low as they define our new list each time
		mid = (low + high) // 2

		#print("low index", low," low value", mylist[low], "high", high,"high value", mylist[high], "mid", mid, "mid value", mylist[mid])

		if mylist[mid] == target:
			result = mid
			high = mid - 1  
		elif mylist[mid] < target:
			#if mid is smaller tha the target then the beginning of our new list is mid + 1 (second side of list)
			high = mid - 1
		else:
			low = mid + 1

	return result


#1.	The target is not in the list
print(binary_search([35,20,16,12,8,5], 25))

#2.	The target is the last element of the list
print(binary_search([35,20,16,12,8,5], 5))

#3.	The target is the first element of the list
print(binary_search([25,20,16,12,8,5], 25))

#4.	The list has only one element (target)
print(binary_search([25], 25))

#4a.The list has only one element ()
print(binary_search([10], 25))

#5.	The list has no elements
print(binary_search([], 25))

#5.	The list has duped numbers
print(binary_search([25,25,25,35,20,16,12,12,5], 25))