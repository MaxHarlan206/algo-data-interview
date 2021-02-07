# RUN LENGTH ENCODING
#O(n) spacetime
def runLengthEncoding(string):
	rlestring = ""
	currval = 0 
	rval = 0 
	counter = 0
	while rval < len(string):
		if string[currval] == string[rval] and counter < 9:
			counter += 1 
			rval += 1 
		else:
			rlestring += str(counter)
			rlestring += str(string[currval])
			currval = rval
			counter = 1 
			rval += 1 	
			
	rlestring += str(counter)
	rlestring += str(string[currval])
	return rlestring

#CAESAR CIPHER ENCRYPTOR 
# O(n) spacetime
def caesarCipherEncryptor(string, key):
	codedlanguage = ""
	alpha = "abcdefghijklmnopqrstuvwxyz"
	key = key % 26
	for letter in string:
		tempval = alpha.find(letter)
		tempval += key
		if tempval > 25:
			tempval = tempval-26
		codedlanguage += alpha[tempval]
	return codedlanguage

# PALINDROME CHECKER 
# O(n) time O(1) space
def isPalindrome(string):
	palindrome = True
	for i in range(len(string)//2):
		if string[i] != string[-(i+1)]:
			palindrome = False
	return palindrome

# SELECTION SORT 
# O(n^2) time O(1) space 
def selectionSort(array):
	unsortstart = 0 
	while(len(array[unsortstart: len(array)-1])) > 0:
		smallest = None
		for i in range(unsortstart, len(array)):
			if smallest == None or array[i] < smallest:
				smallest = array[i]
				smallestidx = i 
		swap(smallestidx, unsortstart, array)
		unsortstart += 1
	return(array)

def swap(i,j, array):
	array[i], array[j] = array[j], array[i]

# BUBBLE SORT 
# O(n^2) time O(1) space 
def bubbleSort(array):
	while 1 == 1:
		isdone = True
		for num in range(len(array)-1):
			prev = array[num]
			if array[num] > array[num + 1]:
				array[num] = array[num+1]
				array[num+1] = prev
				isdone = False
		if isdone == True:
			return array
			break

# NTH FIBONACCI 
# O(n) time O(1) space
def getNthFib(n):
	constants = [0,1]
	if n == 1 or n == 2:
		return constants[n-1]
	if n == 3:
		return sum(constants)
	else: 
		for num in range(n-3):
			newconstants = [0,0]
			newconstants[0] = constants[1]
			newconstants[1] = sum(constants)
			constants = newconstants
		return sum(constants)
	
#Move all instances of an integer to the end of a list (in place) without using the sort algorithm 
# O(n) time O(1) space 
def moveElementToEnd(array, toMove):
	if len(array) < 2:
		return array
	else:
		lpointer = 0 
		rpointer = len(array)-1
	while lpointer < len(array)-1 and rpointer >0 and lpointer < rpointer:
		if array[lpointer] != toMove:
			lpointer += 1 
		if array[rpointer] == toMove:
			rpointer -= 1
		if array[lpointer] == toMove and array[rpointer] != toMove:
			swapnums(lpointer, rpointer, array)
			lpointer += 1 
			rpointer -= 1
	return array
def swapnums(lpointer, rpointer, array):
	array[lpointer], array[rpointer] = array[rpointer], array[lpointer]

# Check if an array is monotonic
# O(n) time O(1) space 
def isMonotonic(array):
	ismonotonic = True 
	if len(array) < 2:
		return ismonotonic
	else:
		lpoint = 0
		rpoint = 1 
	avoiddirection = None
	while avoiddirection == None and rpoint < len(array) - 1:
		if array[lpoint] == array[rpoint]:
			lpoint += 1
			rpoint += 1
		elif array[lpoint] < array[rpoint]:
			avoiddirection = "decrease"
		else: 
			avoiddirection = "increase"
	while rpoint < len(array):
		if array[lpoint] < array[rpoint]:
			currdirection = "increase"
			lpoint +=1
			rpoint +=1
		elif array[lpoint] > array[rpoint]:
			currdirection = "decrease"
			lpoint +=1
			rpoint +=1
		else:
			currdirection = ""
			lpoint +=1
			rpoint +=1
		if currdirection == avoiddirection:
			ismonotonic = False
			break
	return ismonotonic
# Spiral traversing a list of lists
# O(n) Space-time 
def spiralTraverse(array):
    x = -1
	y = 0
	remwidth = len(array[0])
	remheight = len(array)
	spiral_array = []
	
	print(array)
	while remwidth > 0 and remheight > 0:
		# iterate right
		for i in range(remwidth):
			x += 1
			spiral_array.append(array[y][x])
		remheight -= 1 
		if remheight == 0:
			break
		# iterate down
		for i in range(remheight):
			y += 1
			spiral_array.append(array[y][x])
		remwidth -= 1
		if remwidth == 0:
			break
		# iterate left
		for i in range(remwidth):
			x -= 1
			spiral_array.append(array[y][x])
		remheight -= 1 
		if remheight == 0:
			break
		# iterate up 
		for i in range(remheight):
			y -= 1
			spiral_array.append(array[y][x])
		remwidth -= 1
	return spiral_array
