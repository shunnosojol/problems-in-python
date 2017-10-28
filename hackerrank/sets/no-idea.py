#https://www.hackerrank.com/challenges/no-idea/problem
m   = set(map(int,input().split()))
arr = list(map(int,input().split()))
A   = set(map(int,input().split()))
B   = set(map(int,input().split()))

love = 0

for x in arr:
    if x in A:
        love+=1
    if x in B:
        love-=1
print(love)