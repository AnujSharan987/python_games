import pygame, random
from pygame.locals import *


screen =  pygame.display.set_mode([800,600])
pygame.display.set_caption("Cude Racer 2.0")
pygame.display.update()


class cha():
	def __init__(self,x,y,color):
		self.x =x
		self.y =y
		self.sx =0
		self.sy =0
		self.color = color
		self.width=100
		self.height=50
	def update(self):
		pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))
	def pos(self):
		self.x=self.x+self.sx
		self.y=self.y+self.sy


road  = cha(0,200,[0,0,0])
road.width = 900
road.height = 300

o  = cha(600,random.randint(200,400),[255,0,0])
o1  = cha(7850,random.randint(200,400),[0,255,0])
o2  = cha(1050,random.randint(200,400),[255,254,0])
o3  = cha(1250,random.randint(200,400),[255,100,255])
o4  = cha(1450,random.randint(200,400),[205,20,20])
o5  = cha(1650,random.randint(200,400),[225,10,102])
o6  = cha(1850,random.randint(200,400),[18,20,38])
obs = [o,o1,o2,o3,o4,o5,o6]

chare = cha(100,250,[255,255,255])

r=True

while r :
	pygame.time.delay(20)
	screen.fill((0,255,0))
	road.update()
	chare.update()
	chare.pos()
	for e in pygame.event.get():
		if  e.type == QUIT:
			quit()
		if e.type ==  KEYDOWN:
			if e.key == K_LEFT:
				chare.sx-=5
			if e.key == K_RIGHT:
				chare.sx+=5
			if e.key == K_UP:
				chare.sy-=3
			if e.key == K_DOWN:
				chare.sy+=3
		if e.type == KEYUP:
			chare.sx=0
			chare.sy=0
	for b in obs:
		b.update()
		b.x-=5
		if b.x<chare.x+chare.width and b.y>chare.y and b.y<chare.y+chare.height :
			quit()
		if b.x<0:
			b.x = 1950
			b.y = random.randint(200,400)
	pygame.display.update()