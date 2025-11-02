


mylist = [5,7,7,8,8,10,12,13,14,15,16,19,20]
target = 17

def binary_search(mylist, target):
	low, high = 0, len(mylist) -1

	while low <= high:

		mid = (low + high) // 2

		if mylist[mid] == target:
			return mid

		elif mylist[mid] > target:
			high = mid -1
		else:
			low = mid + 1

	return -1


print(binary_search(mylist, target))
