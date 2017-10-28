#https://www.hackerrank.com/challenges/capitalize/problem
def capitalize(string):
    return " ".join([x.capitalize() for x in  string.split(" ")])