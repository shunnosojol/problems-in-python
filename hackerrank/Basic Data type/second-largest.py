#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int,input().strip().split()))[:n]
print(sorted(list(set(arr)))[-2])