#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(s, k):
	n=len(s)
	for x in range(0, n, k):
		slicedStr = s[x : x+k]
		uni =[]
		for y in slicedStr:
			if y not in uni:
				uni.append(y)
		print (''.join(uni))

merge_the_tools("AABCAAADA",3)
