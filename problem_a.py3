/*PROBLEM A: String merging

time limit per test: second

memory limit per test: megabytes

input: standard input

output: standard output

In this problem you will be given two strings - A and B.

Your task is to find a string C such that it contains both A and B as substring and it will be shortest among all possible strings.

A substring of a string is a contiguous subsequence of that string. So, string {kbtu} is substring of string {kbtu open}, but string {fall} is not.

Input Format: The first line of the input will contain string A 1≤∣A∣≤10^5

The second line of the input will contains string B 1≤∣B∣≤10^5

It is guaranteed that both strings will contain only lowercase Latin letters.

Output Format: Print one string - C

Examples: Example 1 {A = compressing, B = single, C = compressingle} Example 2 {A = hi, B = you, C = hiyou}

*/

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

