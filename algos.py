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

