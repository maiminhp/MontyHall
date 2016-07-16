# Name: Minh Pham
# Email: mtp2142@columbia.edu
# module to prove that switching doors in a
# MontyHall gameshow always yields higher chances of winning
########################

import random

def MontyHall(x):
	'''simulates a game of MontyHall, input # of doors'''

	#set prize door, random integer \in [1,x]
	prize = int(random.random()*x + 1)

	#set user selected
	choice = int(random.random()*x + 1)
	
	#show door with no prize
	host = int(random.random()*x + 1)
	while host in [prize,choice]:
		host = int(random.random()*x + 1)

	#switch to another door after hosts open an empty door
	choice_s = int(random.random()*x + 1)
	while choice_s in [choice,host]:
		choice_s = int(random.random()*x + 1)

	no_s_win = False
	s_win = False

	if choice == prize:
		no_s_win = True
	elif choice_s == prize:
		s_win = True

	return s_win, no_s_win

def main():

	games = 10**6
	results = {}

	#print info
	print('\nProbability of two strategies to Monty Hall')
	print('`````````````````````````````````````````````````````````')
	print('{:^10s} {:<25s} {:s}'.format('Doors','Always Switching','Never Switching'))
	print('----------------------------------------------------')

	for i in range(3,10,2):
		sw_win = 0
		no_sw_win = 0
		for j in range(games):
			s_win, no_s_win = MontyHall(i)
			if s_win:
				sw_win += 1
			elif no_s_win:
				no_sw_win += 1
		results[i] = [(sw_win/games),(no_sw_win/games)]
		print('{:^10} {:<25} {}'.format(i, results[i][0], results[i][1]),flush=True)

	return

if __name__ == '__main__':
	main()
