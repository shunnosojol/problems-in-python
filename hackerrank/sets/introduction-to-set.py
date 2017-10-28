#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
    data = list(set(array))
    return sum(data)/len(data)