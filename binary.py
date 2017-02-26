from itertools import permutations
def zbits(n,k):
	#check whether n and k is number and n>k, if it is not, return -1
	if not str(n).isdigit() or not str(k).isdigit():
		print "please input digit"
		return -1
	if k>n:
		print "please input n>k rather than k>n"
		return -1


	#zero represents the k zeros
	zero=''
	#one represents the n-k ones
	one=''
	for i in range(k):
		zero+='0'
	for i in range(n-k):
		one+='1'
	#permutate different combination of 1s and 0s
	permutation_string_list = []
	for elements in permutations(zero+one):
		string_elements=''
		for element in elements:
			string_elements+=element
		permutation_string_list.append(string_elements)
	#the final return set
	final_binay_string_set = set(permutation_string_list)
	return final_binay_string_set

print zbits(4,3)
print zbits(4,1)
print zbits(5,4)
print zbits('t',4)
print zbits(3,5)