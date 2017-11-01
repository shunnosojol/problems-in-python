#https://www.hackerrank.com/challenges/py-set-add/problem

inp= int(input())
country = set()
for x in range(inp):
    country.add(input())
print(len(country))

#Second example
print(len(set([ str(input()) for _ in range(int(input()))])))