#https://www.hackerrank.com/challenges/symmetric-difference/problem
_ , M = input(), set(map(int,input().split()))
_ , N = input(), set(map(int,input().split()))

print ('\n'.join(sorted([str(x) for x in list(M^N)],key=int)))


