import os

from headers import *
from utility import * 
from input import *
import time
#os.system('clear')

obj_board.paddle()
obj_board.ball()
#obj_board.brick()
flag=0
Lives1=3
Lives=3
Score=0
start_time=time.time()

#paddle()

while(1):
	if(Lives!=0):

		os.system('clear')
		Lives=obj_board.Lives(Lives)
		if(Lives!=Lives1):
			obj_board.ball()
			obj_board.paddle()
			Lives1=Lives1-1
		Score=obj_board.score(Score)
		#time=GAMETIME-(round(time.time()) - round(start_time))
		newtime = GAMETIME + (round(time.time()) - round(start_time))
		print("Lives:",Lives,"                                                   ","scores",Score,"                                                      ","time:",newtime)
		obj_board.print_board(factor)
		obj_board.brick()
		obj_board.expand_paddle(newtime)
		obj_board.normal_paddle(newtime)
		obj_board.shrink_paddle(newtime)
		obj_board.normal_paddle2(newtime)
		obj_board.thru_ball(newtime)
		obj_board.normal_ball(newtime)
		flag=obj_board.grab_ball(newtime,flag)
		flag=obj_board.release_ball(newtime,flag)
		#Lives=obj_board.Lives(Lives)
		if flag == 1:
			obj_board.ballmovement()	
		input = input_to()
		#print(input)
		if input == 'a':
			obj_board.paddle_left()
		if input == 'd':
			obj_board.paddle_right()
		if input =='s':
			flag=1
	else:
		print("thanks for playing")
		quit()

	#obj_board.ballmovement()
	#obj_board.print_board(factor)