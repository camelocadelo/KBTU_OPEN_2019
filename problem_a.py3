
str1 = input()
str2 = input()


def my_concatenate(s1, s2):
    i = 0
    while not s2.startswith(s1[i:]):
        i += 1
    return s1[:i] + s2
    
def my_function(a, b):
	if (a in b):
		return b
	elif (b in a):
		return a
	else:
		result1 = my_concatenate(a, b)
		result2 = my_concatenate(b, a)
		if (len(result1) > len(result2)):
			return result2
		elif (len(result2) > len(result1)):
			return result1
		elif (len(result1) == len(result2)):
			return result1
		
print(my_function(str1, str2))

