from headers import *
from colorama import Fore,Back,Style
import time

class Board:

    #Creates the entire board for the game

    #constructor function
    def __init__(self, rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.grid=[]
        self.__flag=0
        self._x=rows-2
        self._dim1=90
        self._dim2=110
        self._bx=rows-3
        self._by=100
        self._flag=1
        self._lr1=0
        self._lr2=0
        self._tb1=0
        self._tb2=0
        self._c1=1
        self._b1x=10
        self._b1y=50
        self._c2=3
        self._b2x=10
        self._b2y=63
        self._c3=2
        self._b3x=10
        self._b3y=76
        self._c4=1
        self._b4x=10
        self._b4y=89
        self._c5=2
        self._b5x=10
        self._b5y=102
        self._c6=3
        self._b6x=10
        self._b6y=115
        self._c7=1
        self._b7x=10
        self._b7y=128
        self._c8=2
        self._b8x=10
        self._b8y=141
        self._c9=3
        self._b9x=15
        self._b9y=63
        self._c10=1
        self._b10x=15
        self._b10y=76
        self._c11=2
        self._b11x=15
        self._b11y=89
        self._c12=1
        self._b12x=15
        self._b12y=102
        self._c13=2
        self._b13x=15
        self._b13y=115
        self._c14=3
        self._b14x=15
        self._b14y=128
        self._c15=2
        self._b15x=20
        self._b15y=76
        self._c16=1
        self._b16x=20
        self._b16y=89
        self._c17=3
        self._b17x=20
        self._b17y=102
        self._c18=1
        self._b18x=20
        self._b18y=115
        self._score=0
        self._ub1x=15
        self._ub1y=37
        self._ub2x=15
        self._ub2y=154
        self._pc1=0
        self._pb1x=20
        self._pb1y=50
        self._pc2=0
        self._pb2x=20
        self._pb2y=141
        self._pc3=0
        self._pb3x=10
        self._pb3y=24
        self._pc4=0
        self._pb4x=10
        self._pb4y=167
        self._paddlelen=20
        self._p1=0
        self._p2=0
        self._p3=0
        self._p4=0
        self._t1=0
        self._t2=0
        self._t3=0
        self._t4=0
        self._uc1=0
        self._uc2=0






    
    #function to create the playing board
    def create_board(self):
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                self.temp.append(" ")
            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)
        

    #function to print the playing board
    def print_board(self, factor):
            for i in range(self.__rows):
                for j in range (factor, SCREEN+factor):
                    
                    # print(Back.LIGHTBLACK_EX +self.grid[i][j] + Back.RESET, end='')
                    print(self.grid[i][j],end='')
                    
                print()
    
    def paddle(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                #print(self.__rows)
                #print(self.__cols)
                '''if(j<self.__cols-1):
                    self.grid[i][j]="a"
                if(j==self.__cols-30):
                    self.grid[i][j]=="b"'''
                if(i==self.__rows-2):
                    if(j>90 and j<110):
                        self._x=self.__rows-2
                        self._dim1=90
                        self._dim2=110
                        self.grid[i][j]="b"
    def paddle_left(self):
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                self.grid[i][j]=" "
        const=3
        if(self._dim1-const > 2 ):
            for i in range(self._paddlelen):
                self.grid[self._x][self._dim1-const]="b"
                const=const+1

            self._dim1=self._dim1-const
            self._dim2=self._dim1+20
        else:
            for i in range(self._paddlelen):
                self.grid[self._x][self._dim1]="b"
                self._dim1=self._dim1+1

    def paddle_right(self):
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                self.grid[i][j]=" "
        const=3
        if(self._dim2+const < self.__cols-102):
            for i in range(self._paddlelen):
                self.grid[self._x][self._dim2+const]="b"
                const=const+1
            self._dim2=self._dim2+const
            self._dim1=self._dim2-20
        else:
            for i in range(self._paddlelen):
                self.grid[self._x][self._dim2]="b"
                self._dim1=self._dim2-1

    def ball(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if(i==self.__rows-3 and j==100):
                    self._bx=self.__rows-3
                    self._by=100
                    self.grid[i][j]="o"
    def ballmovement(self): 
        #print(self._by)       
        if(self._bx == self.__rows-3):
            if(self._by > self._dim1 and self._by < self._dim2):
                if(self._lr1==0):
                    self._flag=1
                    self._lr1=1
                elif(self._lr1==1):
                    self._flag=4
                    self._lr1=2
                elif(self._lr1==2):
                    self._flag=6
                    self._lr1=0

        if(self._bx==2):
            if(self._lr2==0):
                self._flag=7
                self._lr2=1
            elif(self._lr2==1):
                self._flag=5
                self._lr2=2
            elif(self._lr2==2):
                self._flag=0
                self._lr2=0

        if(self._by >= self.__cols-100 ):
            if(self._tb1==0):
                self._flag=2
                self._tb1=1
            elif(self._tb1==1):
                self._flag=8
                self._tb1=2
            elif(self._tb1==2):
                self._flag=9
                self._tb1=0

        if(self._by<=2):
            if(self._tb2==0):
                self._flag=3
                self._tb2=1
            elif(self._tb2==1):
                self._flag=10
                self._tb2=2
            elif(self._tb2==2):
                self._flag=11
                self._tb2=0
        if(self._c1!=0):
            if(self._bx >= self._b1x-1 and self._bx <= self._b1x+4):
                if(self._by >= self._b1y-1 and self._by <= self._b1y+11):
                    self._c1=self._c1-1
                    self._score=self._score+1
                    #print(self._flag)
                    if(self._p1==1):
                        self._c1=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b1y-1 or self._by==self._b1y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b1y-1 or self._by==self._b1y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b1y+11 or self._by==self._b1y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b1y+11 or self._by==self._b1y+10):
                            self._flag=1
                        else:
                            self._flag=5
                    #print(self._flag)

        if(self._c2!=0):
            if(self._bx >= self._b2x-1 and self._bx <= self._b2x+4):
                if(self._by >= self._b2y-1 and self._by <= self._b2y+11):
                    self._c2=self._c2-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c2=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b2y-1 or self._by==self._b2y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b2y-1 or self._by==self._b2y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b2y+11 or self._by==self._b2y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b2y+11 or self._by==self._b2y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c3!=0):
            if(self._bx >= self._b3x-1 and self._bx <= self._b3x+4):
                if(self._by >= self._b3y-1 and self._by <= self._b3y+11):
                    self._c3=self._c3-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c3=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b3y-1 or self._by==self._b3y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b3y-1 or self._by==self._b3y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b3y+11 or self._by==self._b3y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b3y+11 or self._by==self._b3y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c4!=0):
            if(self._bx >= self._b4x-1 and self._bx <= self._b4x+4):
                if(self._by >= self._b4y-1 and self._by <= self._b4y+11):
                    self._c4=self._c4-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c4=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b4y-1 or self._by==self._b4y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b4y-1 or self._by==self._b4y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b4y+11 or self._by==self._b4y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b4y+11 or self._by==self._b4y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c5!=0):
            if(self._bx >= self._b5x-1 and self._bx <= self._b5x+4):
                if(self._by >= self._b5y-1 and self._by <= self._b5y+11):
                    self._c5=self._c5-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c5=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b5y-1 or self._by==self._b5y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b5y-1 or self._by==self._b5y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b5y+11 or self._by==self._b5y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b5y+11 or self._by==self._b5y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c6!=0):
            if(self._bx >= self._b6x-1 and self._bx <= self._b6x+4):
                if(self._by >= self._b6y-1 and self._by <= self._b6y+14):
                    self._c6=self._c6-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c6=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b6y-1 or self._by==self._b6y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b6y-1 or self._by==self._b6y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b6y+11 or self._by==self._b6y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b6y+11 or self._by==self._b6y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c7!=0):
            if(self._bx >= self._b7x-1 and self._bx <= self._b7x+4):
                if(self._by >= self._b7y-1 and self._by <= self._b7y+11):
                    self._c7=self._c7-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c7=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b7y-1 or self._by==self._b7y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b7y-1 or self._by==self._b7y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b7y+11 or self._by==self._b7y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b7y+11 or self._by==self._b7y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c8!=0):
            if(self._bx >= self._b8x-1 and self._bx <= self._b8x+4):
                if(self._by >= self._b8y-1 and self._by <= self._b8y+11):
                    self._c8=self._c8-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c8=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b8y-1 or self._by==self._b8y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b8y-1 or self._by==self._b8y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b8y+11 or self._by==self._b8y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b8y+11 or self._by==self._b8y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c9!=0):
            if(self._bx >= self._b9x-1 and self._bx <= self._b9x+4):
                if(self._by >= self._b9y-1 and self._by <= self._b9y+11):
                    self._c9=self._c9-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c9=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b9y-1 or self._by==self._b9y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b9y-1 or self._by==self._b9y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b9y+11 or self._by==self._b9y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b9y+11 or self._by==self._b9y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c10!=0):
            if(self._bx >= self._b10x-1 and self._bx <= self._b10x+4):
                if(self._by >= self._b10y-1 and self._by <= self._b10y+11):
                    self._c10=self._c10-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c10=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b10y-1 or self._by==self._b10y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b10y-1 or self._by==self._b10y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b10y+11 or self._by==self._b10y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b10y+11 or self._by==self._b10y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c11!=0):
            if(self._bx >= self._b11x-1 and self._bx <= self._b11x+4):
                if(self._by >= self._b11y-1 and self._by <= self._b11y+11):
                    self._c11=self._c11-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c11=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b11y-1 or self._by==self._b11y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b11y-1 or self._by==self._b11y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b11y+11 or self._by==self._b11y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b11y+11 or self._by==self._b11y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c12!=0):
            if(self._bx >= self._b12x-1 and self._bx <= self._b12x+4):
                if(self._by >= self._b12y-1 and self._by <= self._b12y+11):
                    self._c12=self._c12-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c12=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b12y-1 or self._by==self._b12y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b12y-1 or self._by==self._b12y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b12y+11 or self._by==self._b12y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b12y+11 or self._by==self._b12y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c13!=0):
            if(self._bx >= self._b13x-1 and self._bx <= self._b13x+4):
                if(self._by >= self._b13y-1 and self._by <= self._b13y+11):
                    self._c13=self._c13-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c13=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b13y-1 or self._by==self._b13y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b13y-1 or self._by==self._b13y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b13y+11 or self._by==self._b13y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b13y+11 or self._by==self._b13y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c14!=0):
            if(self._bx >= self._b14x-1 and self._bx <= self._b14x+4):
                if(self._by >= self._b14y-1 and self._by <= self._b14y+11):
                    self._c14=self._c14-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c14=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b14y-1 or self._by==self._b14y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b14y-1 or self._by==self._b14y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b14y+11 or self._by==self._b14y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b14y+11 or self._by==self._b14y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c15!=0):
            if(self._bx >= self._b15x-1 and self._bx <= self._b15x+4):
                if(self._by >= self._b15y-1 and self._by <= self._b15y+11):
                    self._c15=self._c15-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c15=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b15y-1 or self._by==self._b15y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b15y-1 or self._by==self._b15y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b15y+11 or self._by==self._b15y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b15y+11 or self._by==self._b15y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c16!=0):
            if(self._bx >= self._b16x-1 and self._bx <= self._b16x+4):
                if(self._by >= self._b16y-1 and self._by <= self._b16y+11):
                    self._c16=self._c16-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c16=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b16y-1 or self._by==self._b16y ):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b16y-1 or self._by==self._b16y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b16y+11 or self._by==self._b16y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b16y+11 or self._by==self._b16y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._c17!=0):
            if(self._bx >= self._b17x-1 and self._bx <= self._b17x+4):
                if(self._by >= self._b17y-1 and self._by <= self._b17y+11):
                    self._c17=self._c17-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c17=0
                    #print(self._flag)

                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b17y-1 or self._by==self._b17y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b17y-1 or self._by==self._b17y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b17y+11 or self._by==self._b17y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b17y+10 or self._by==self._b17y+10):
                            self._flag=1
                        else:
                            self._flag=5
                    #print(self._flag)
        if(self._c18!=0):
            if(self._bx >= self._b18x-1 and self._bx <= self._b18x+4):
                if(self._by >= self._b18y-1 and self._by <= self._b18y+11):
                    self._c18=self._c18-1
                    self._score=self._score+1
                    if(self._p1==1):
                        self._c18=0
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._b18y-1 or self._by==self._b18y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._b18y-1 or self._by==self._b18y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._b18y+11 or self._by==self._b18y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._b18y+11 or self._by==self._b18y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._pc1==0):
            if(self._bx >= self._pb1x-1 and self._bx <= self._pb1x+4):
                if(self._by >= self._pb1y-1 and self._by <= self._pb1y+11):
                    self._pc1=1
                    self._flag=7
        if(self._pc2==0):
            if(self._bx >= self._pb2x-1 and self._bx <= self._pb2x+4):
                if(self._by >= self._pb2y-1 and self._by <= self._pb2y+11):
                    self._pc2=1
                    self._flag=7
        if(self._pc3==0):
            if(self._bx >= self._pb3x-1 and self._bx <= self._pb3x+4):
                if(self._by >= self._pb3y-1 and self._by <= self._pb3y+11):
                    self._pc3=1
                    self._flag=7
        if(self._pc4==0):
            if(self._bx >= self._pb4x-1 and self._bx <= self._pb4x+4):
                if(self._by >= self._pb4y-1 and self._by <= self._pb4y+11):
                    self._pc4=1
                    self._flag=7
        if(self._uc1==0):
            if(self._bx >= self._ub1x-1 and self._bx <= self._ub1x+4):
                if(self._by >= self._ub1y-1 and self._by <= self._ub1y+14):
                    if(self._p1==1):
                        self._uc1=1
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._ub1y-1 or self._by==self._ub1y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._ub1y-1 or self._by==self._ub1y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._ub1y+11 or self._by==self._ub1y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._ub1y+11 or self._by==self._ub1y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._uc2==0):
            if(self._bx >= self._ub2x-1 and self._bx <= self._ub2x+4):
                if(self._by >= self._ub2y-1 and self._by <= self._ub2y+14):
                    if(self._p1==1):
                        self._c1=1
                    elif(self._flag==6):
                        self._flag=7
                    elif(self._flag==7):
                        self._flag=6
                    elif(self._flag==9):
                        self._flag=11
                    elif(self._flag==11):
                        self._flag=9
                    elif(self._flag==1 or self._flag==10):
                        if(self._by==self._ub2y-1 or self._by==self._ub2y):
                            self._flag=2
                        else:
                            self._flag=0
                    elif(self._flag==0 or self._flag==3):
                        if(self._by==self._ub2y-1 or self._by==self._ub2y):
                            self._flag=5
                        else:
                            self._flag=1
                    elif(self._flag==5 or self._flag==8):
                        if(self._by==self._ub2y+11 or self._by==self._ub2y+10):
                            self._flag=0
                        else:
                            self._flag=2
                    elif(self._flag==2 or self._flag==4):
                        if(self._by==self._ub2y+11 or self._by==self._ub2y+10):
                            self._flag=1
                        else:
                            self._flag=5
        if(self._flag==0):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx+1][self._by+3]="o"
            self._bx=self._bx+1
            self._by=self._by+3
        if(self._flag==1):           
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx-1][self._by+2]="o"
            self._bx=self._bx-1
            self._by=self._by+2
        if(self._flag==2):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx-1][self._by-3]="o"
            self._bx=self._bx-1
            self._by=self._by-3
        if(self._flag==3):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx+1][self._by+3]="o"
            self._bx=self._bx+1
            self._by=self._by+3
        if(self._flag==4):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx-1][self._by-3]="o"
            self._bx=self._bx-1
            self._by=self._by-3
        if(self._flag==5):
            self.grid[self._bx][self._by]=" "
            if(self._by-3 <= 3):
                self.grid[self._bx+1][self._by-1]="o"
                self._by=self._by-1
            else:
                self.grid[self._bx+1][self._by-3]="o"
                self._by=self._by-3
            self._bx=self._bx+1
            
        if(self._flag==6):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx-1][self._by]="o"
            self._bx=self._bx-1
            self._by=self._by
        if(self._flag==7):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx+1][self._by]="o"
            self._bx=self._bx+1
            self._by=self._by
        if(self._flag==8):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx+1][self._by-3]="o"
            self._bx=self._bx+1
            self._by=self._by-3
        if(self._flag==9):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx][self._by-3]="o"
            self._bx=self._bx
            self._by=self._by-3
        if(self._flag==10):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx-1][self._by+3]="o"
            self._bx=self._bx-1
            self._by=self._by+3
        if(self._flag==11):
            self.grid[self._bx][self._by]=" "
            self.grid[self._bx][self._by+3]="o"
            self._bx=self._bx
            self._by=self._by+3

    
    def brick(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if( i>=10 and i <13):
                    if(self._pc3==0):
                        if(j>=24 and j<=34):
                            self.grid[i][j]=Back.BLUE+"#"+Back.RESET
                    if(self._pc3==1):
                        if(j>=24 and j<=34):
                            self.grid[i][j]=" "
                    if(self._c1==1):
                        if(j >=50  and j <= 60):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c1==0):
                        if(j >=50  and j <= 60):
                            self.grid[i][j]=" "
                    if(self._c2==3):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=Back.RED+"#"+Back.RESET
                    if(self._c2==2):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c2==1):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c2==0):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=" "
                    if(self._c3==2):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c3==1):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c3==0):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=" "
                    if(self._c4==1):
                        if( j >= 89 and j <= 99):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c4==0):
                        if( j >= 89 and j <= 99):
                            self.grid[i][j]=" "
                    if(self._c5==2):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c5==1):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c5==0):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=" "
                    if(self._c6==3):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=Back.RED+"#"+Back.RESET
                    if(self._c6==2):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c6==1):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c6==0):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=" "
                    if(self._c7 ==1):
                        if(j >= 128 and j <= 138):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c7 ==0):
                        if(j >= 128 and j <= 138):
                            self.grid[i][j]=" "
                    if(self._c8==2):    
                        if(j >= 141 and j <= 151):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c8==1):    
                        if(j >= 141 and j <= 151):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c8==0):    
                        if(j >= 141 and j <= 151):
                            self.grid[i][j]=" "
                    if(self._pc4==0):
                        if(j>=167 and j<=177):
                            self.grid[i][j]=Back.BLUE+"#"+Back.RESET
                    if(self._pc4==1):
                        if(j>=167 and j<=177):
                            self.grid[i][j]=" "


                if(i >=15 and i < 18):
                    if(self._uc1==0):
                        if( j >= 37 and j<=47 ):
                            self.grid[i][j]=Back.LIGHTMAGENTA_EX + "#" + Back.RESET
                    if(self._uc1==1):
                        if( j >= 37 and j<=47 ):
                            self.grid[i][j]=" "
                    if(self._c9==3):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=Back.RED+"#"+Back.RESET
                    if(self._c9==2):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c9==1):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c9==0):
                        if( j >= 63 and j <= 73):
                            self.grid[i][j]=" "
                    if(self._c10==1):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c10==0):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=" "
                    if(self._c11==2):
                        if( j >= 89 and j <= 99):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c11==1):
                        if( j >= 89 and j <= 99):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c11==0):
                        if( j >= 89 and j <= 99):
                            self.grid[i][j]=" "
                    if(self._c12==1):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c12==0):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=" "
                    if(self._c13==2):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c13==1):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c13==0):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=" "
                    if(self._c14 ==3):
                        if(j >= 128 and j <= 138):
                            self.grid[i][j]=Back.RED+"#"+Back.RESET
                    if(self._c14 ==2):
                        if(j >= 128 and j <= 138):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c14 ==1):
                        if(j >= 128 and j <= 138):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c14 ==0):
                        if(j >= 128 and j <= 138):
                            self.grid[i][j]=" "
                    if(self._uc2==0):
                        if( j >= 154 and j<=164 ):
                            self.grid[i][j]=Back.LIGHTMAGENTA_EX + "#" + Back.RESET
                    if(self._uc2==1):
                        if( j >= 154 and j<=164 ):
                            self.grid[i][j]=" "
                if(i >= 20 and i < 23):
                    if(self._pc1==0):
                        if(j >=50  and j <= 60):
                                self.grid[i][j]=Back.BLUE+"#"+Back.RESET
                    if(self._pc1==1):
                        if(j >=50  and j <= 60):
                                self.grid[i][j]=" "
                    if(self._c15==2):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c15==1):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c15==0):
                        if(j >=76 and  j <= 86):
                            self.grid[i][j]=" "
                    if(self._c16==1):
                        if( j >= 89 and j <= 99):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c16==0):
                        if( j >= 89 and j <= 99):
                            self.grid[i][j]=" "
                    if(self._c17==3):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=Back.RED+"#"+Back.RESET
                    if(self._c17==2):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=Back.YELLOW+"#"+Back.RESET
                    if(self._c17==1):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c17==0):
                        if( j >= 102 and j<=112):
                            self.grid[i][j]=" "
                    if(self._c18==1):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=Back.GREEN+"#"+Back.RESET
                    if(self._c18==0):
                        if( j >= 115 and j <= 125):
                            self.grid[i][j]=" "
                    if(self._pc2==0):
                        if(j >= 141 and j <= 151):
                            self.grid[i][j]=Back.BLUE+"#"+Back.RESET
                    if(self._pc2==1):
                        if(j >= 141 and j <= 151):
                            self.grid[i][j]=" "

    def Lives(self,Lives):
        if(self._bx == self.__rows-3):
            if(self._by > self._dim1 and self._by < self._dim2):
                return Lives
            else:
                self.grid[self._bx][self._by]=" "
                for i in range(self.__rows):
                    for j in range(self.__cols):
                        if(i==self.__rows-2):
                            if(j>self._dim1 and j<self._dim2):
                                self.grid[i][j]=" "
                Lives=Lives-1
                return Lives
        else:
            return Lives
    def score(self,score):
        score=self._score
        return score
    def expand_paddle(self,newtime):
        if(self._pc3==1):
            if(self._bx == self.__rows-3):
                if(self._by > self._dim1 and self._by < self._dim2):
                    self._t1=newtime
                    self._p3=1
                    self._paddlelen=self._paddlelen+5
                    self._pc3=5
    def normal_paddle(self,newtime):
        if(self._p3==1):
            if(newtime-self._t1>10):
                self._paddlelen=self._paddlelen-5
                self._p3=0
    def shrink_paddle(self,newtime):
        if(self._pc4==1):
            if(self._bx == self.__rows-3):
                if(self._by > self._dim1 and self._by < self._dim2):
                    self._t2=newtime
                    self._p4=1
                    self._paddlelen=self._paddlelen-5
                    self._pc4=5
    def normal_paddle2(self,newtime):
        if(self._p4==1):
            if(newtime-self._t2>10):
                self._paddlelen=self._paddlelen+5
                self._p4=0
    def thru_ball(self,newtime):
        if(self._pc1==1):
            if(self._bx == self.__rows-3):
                if(self._by > self._dim1 and self._by < self._dim2):
                    self._p1=1
                    self._t3=newtime
                    self._pc1=5
    def normal_ball(self,newtime):
        if(self._p1==1):
            if(newtime-self._t3 > 10):
                self._p1=0
    def grab_ball(self,newtime,flag):
        if(self._pc2==1):
            if(self._bx == self.__rows-3):
                if(self._by > self._dim1 and self._by < self._dim2):
                    self.grid[self._bx][self._by]="o"
                    flag=0
                    self._p2=1
                    self._pc2=5
                    self._t4=newtime
                    return flag
                else:
                    return flag
            else:
                return flag
        else:
            return flag
    def release_ball(self,newtime,flag):
        if(self._p2==1):
            if(newtime-self._t4>10):
                flag=1
                self._p2=0
                return flag
            else:
                return flag
        else:
            return flag

