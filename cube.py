import pygame, random
screen = pygame.display.set_mode((900, 700))
pygame.init()
import numpy as np
class spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
       
       
    def show(self, color, st):
    	pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
    	pygame.display.update()


class Run:
	def __init__(self):
		self.array = self.generateArray()
		self.color = (0, 255, 0)
		self.grey = (220, 220, 220)
		self.cols = 300
		self.grid = [0 for i in range(self.cols)]
		self.row = 300
		self.max_n = max(self.array)
		self.w = 900/self.cols
		self.h = 700/self.row
		
	def generateArray(self):
		return np.random.randint(1,100,100)
	
	def display(self):
		global w,h
		w = self.w
		h = self.h
		screen.fill((255,255,255))
		for i in range(self.cols):
			self.grid[i] = [0 for i in range(self.row)]

		# Create Spots
		for i in range(self.cols):
		    for j in range(self.row):
		        self.grid[i][j] = spot(i, j)

		#for i in range(self.cols):
		 #   for j in range(self.row):
		  #      self.grid[i][j].show((255, 255, 255), 0)

		for j in range(len(self.array)):
			x = self.array[j]
			#pygame.time.delay(80)
			for i in range(x):
					self.grid[(self.cols//3)+j][self.max_n-i+(self.row//2)].show(self.color, 1)
		return self.array

	def remove(self,item,position):
		#pygame.time.delay(100)
		for i in range(item):
			self.grid[(self.cols//3)+position][self.max_n-i+(self.row//2)].show((255, 255, 255), 0)
        
	def add(self,item,position):
		#pygame.time.delay(100)
		for i in range(item):
			self.grid[(self.cols//3)+position][self.max_n-i+(self.row//2)].show(self.color, 1)

				
	   


