https://www.hackerrank.com/challenges/no-idea/problem

happiness = 0 
nums = input().split()
nums = list(map(int, nums))
n = input().split()
arr = list(map(int, n))

a = input().split()
a = set(map(int, a))

b = input().split()
b = set(map(int, b))


for num in arr:
    if num in a:
        happiness +=1
    elif num in b:
        happiness -=1

print(happiness)
