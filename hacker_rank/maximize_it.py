from itertools import product

k, m = (int(num) for num in input().split())

superlist = []

for i in range(k):
    superlist.append([int(i) for i in input().split()[1:]])
    
# get all permutations without figuring out complicated nested for-loop
ps = product(*superlist)

# function: f(x) = x**2 and {f(a0)+f(a1)+...+f(an)} % m 
maxes = [sum([i**2 for i in product]) % m for product in ps]

print(max(maxes))
