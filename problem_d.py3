/*Problem D: Students love
  Link to the task: https://tau.moe/problemset/task/9/
      
time limit per test:	1.0 second
memory limit per test:	256 megabytes
input:	standard input
output:	standard output
Nurdaulet and Zharaskhan are coaching students. To each student they have their own attitudes, it can be 
expressed as number a_i (for Nurdaulet) and b_i (for Zharaskan) that are called live index of students. 
Askar asked them to calculate the unfair attitude rate. Unfair attitude rate is the difference between the largest
and the smallest love index. In order to not show their possibly large unfair attitude rates, they decided to cheat: 
each shuffle his array, then form new array c_i = a_i + b_i and show the rate of new formed array to Askar. 
What is the minimal possible rate they can achieve?

Input Format:
On the first line you are given single integer n (1≤n≤200000).
On the second line you are given n integers a_i (−10^6 ≤ a_i ≤10^6)
On the third line you are given n integers b_i (−10^6 ≤b_i ≤10^6)

Output Format:
Output single integer, the answer to the problem
*/

input1 = input()
input_a = input()
input_b = input()

a = list(map(int, input_a.split()))
b = list(map(int, input_b.split()))

a.sort(reverse = True)
b.sort()

c = [x + y for x, y in zip(a, b)]

min = min(c)
max = max(c)

result = (abs(max-min))

print(result)

