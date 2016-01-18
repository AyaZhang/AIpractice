"""
Author:
Xinyi Ma xim002@ucsd.edu
Yijun Zhang yiz160@ucsd.edu
Yuanchi Ha yuha@ucsd.edu
"""

import sys
import fileinput
from collections import deque

lineNum = 0
for line in fileinput.input():
	try:
		arrangment[lineNum] = [int(x.strip()) for x in line.split(',')]
		length[lineNum] = len(arrangment[lineNum])
		lineNum += 1
	except:
		sys.exit('invalid input')

	# Initial state not 0 or 1
	for i in range(0, lineNum):
		for k in range(0, length[lineNum] - 1):
			if arrangement[i][k] not in [0,1]:
				sys.exit('invalid input')

	# Whether the state is a goal state
	for i in range(0, lineNum):
		for k in range(0, length[lineNum] - 1):
			if arrangement[i][k] is 0:
				continue
			else:
				sys.exit('False')
	print('True')

sys.exit()
