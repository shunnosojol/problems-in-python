https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
	vowels = 'AEIOU'
	stusc = 0
	kevsc = 0

	for i in range(len(string)):
	    if string[i] in vowels:
	        kevsc += (len(string)-i)
	    else:
	        stusc += (len(string)-i)

	if kevsc > stusc:
		print("Kevin", kevsc)
	elif kevsc < stusc:
		print ("Stuart", stusc)
	else:
		print("Draw")

minion_game("BANANA")