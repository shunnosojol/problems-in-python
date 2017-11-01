#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n = int(input())
role_en = set(map(int,input().split()))
b = int(input())
role_french = set(map(int,input().split()))
print(len(role_en & role_french))