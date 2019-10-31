#Problem C: Boring GCD

#Link to the problem: https://tau.moe/problemset/task/8/
	
/*time limit per test:	2.0 second
memory limit per test:	512 megabytes
input:	standard input
output:	standard output
You are given an array a_1, a_2, a_3 .. a_n

There are 4 types of operations with it:

    • 1 l r x, for each i ∈ [l,r] replace a_i with the value of x
    • 2 l r x, for each i ∈ [l,r] replace a_i with the value of gcd(a_i, x) function
    • 3 l r, output the value of max_{i∈[l,r]} a_i
    • 4 l r, output the value of ∑_{i∈[l,r]} a_i	
 
Greatest common divisor gcd(a,b) of two positive integers a and b is equal to the biggest integer d such that
both integers a and b are divisible by d.

Input Format:
The first line contains two integers n, q (1≤n,m≤10^5) - the number of array elements and the number of queries.
The second line contains n positive integers a_1, a_2, .., a_n - initial state of the array.
Next m lines contain the description of the queries, one per line. 
Queries are formatted the same way as in the problem statement above.

It is guaranteed that 1≤l≤r≤n and 1≤x≤10^9 
 
Output Format:
For each 3rd and 4th query type output answer for this query in a separate line.

Examples:
#Input	
1	
5 11
1 6 8 7 3
3 1 5
4 1 5
2 1 5 6
3 1 5
4 2 4
1 1 5 10
3 1 4
4 3 5
2 3 4 3
3 2 3
4 4 5

#Output
8
25
6
9
10
30
10
11 */

import math

len_queries = input()

len_queries = list(map(int, len_queries.split()))

length = len_queries[0]

queries = len_queries[1]

my_array = input()

my_array = list(map(int, my_array.split()))

queries_list = []


for i in range(queries):
	temp_input = input()
	temp_input = list(map(int, temp_input.split()))
	queries_list.append(temp_input)

for el in queries_list:
	if el[0] == 1:
		l = el[1]
		r = el[2]
		x = el[3]
		my_array[l-1:r] = [x for i in range(r-l+1)]
	elif el[0] == 2:
		l = el[1]
		r = el[2]
		x = el[3]
		my_array[l-1:r] = [math.gcd(my_array[i], x) for i in range(r-l+1)]
	elif el[0] == 3:
		l = el[1]
		r = el[2]
		copy_array = my_array[l-1: r]
		max_value = max(copy_array)
		print(max_value)
	elif el[0] == 4:
		l = el[1]
		r = el[2]
		copy_array_2 = my_array[l-1: r]
		sum_value = sum(copy_array_2)
		print(sum_value)
		
