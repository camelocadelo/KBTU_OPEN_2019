
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
		
