#Практическая работа
import pygame
pygame.init()

WIDTH=400
HEIGHT=400
DARK_GRAY=(128,128,128)
GRAY=(192,192,192)
WHITE=(255,255,255)
FPS=140
color=GRAY

sc=pygame.display.set_mode((WIDTH,HEIGHT))
sc.fill(WHITE)

rect1=pygame.Rect((0,0,WIDTH//2,HEIGHT//2))
rect2=pygame.Rect((WIDTH//2,0,WIDTH//2,HEIGHT//2))
rect3=pygame.Rect((WIDTH//2,HEIGHT//2,WIDTH//2,HEIGHT//2))
rect4=pygame.Rect((0,HEIGHT//2,WIDTH//2,HEIGHT//2))

sc1=pygame.Surface((WIDTH//2,HEIGHT//2))
sc2=pygame.Surface((WIDTH//2,HEIGHT//2))
sc3=pygame.Surface((WIDTH//2,HEIGHT//2))
sc4=pygame.Surface((WIDTH//2,HEIGHT//2))

sc1.fill(WHITE)
sc2.fill(WHITE)
sc3.fill(WHITE)
sc4.fill(WHITE)
 
sc.blit(sc1, rect1)
sc.blit(sc2, rect2)
sc.blit(sc3, rect3)
sc.blit(sc4, rect4)

a=(rect1,rect2,rect3,rect4)

pygame.draw.circle(sc,color,(WIDTH//2,HEIGHT//2),100)
clock=pygame.time.Clock()
pygame.display.flip()

while 1:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			pygame.quit()
			break
		elif i.type==pygame.KEYDOWN:
			if i.key==pygame.K_1:
				a=(rect1,rect3)
			elif i.key==pygame.K_2:
				a=(rect2,rect4)
			elif i.key==pygame.K_0:
				a=(rect1,rect2,rect3,rect4)
			clock.tick(FPS)
	if True:
		if color==GRAY:
			color=DARK_GRAY
		elif color==DARK_GRAY:
			color=GRAY
		pygame.draw.circle(sc,color,(WIDTH//2,HEIGHT//2),100)
		pygame.display.update(a)
		pygame.time.delay(500)
	clock.tick(FPS)

















































