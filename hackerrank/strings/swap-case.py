#https://www.hackerrank.com/challenges/swap-case/problem
# First Way
def swap_case(s):
    text = []
    for n in s:
        if n == n.lower():
            text.append(n.upper())
        else:
            text.append(n.lower())
    return ''.join(text)

#second Way 
def swap_case(s):
	return " ".join([x.lower() if x.isupper() else x.upper() for x in s])