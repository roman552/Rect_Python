import pygame
pygame.init()

sc=pygame.display.set_mode((400,400))

rect1=pygame.Rect((0,0,30,30))
rect2=pygame.Rect((30,30,30,30))

print(rect1.bottomright) #вывод (30,30)
print(rect2.bottomright) #(60,60)

rect2.move_ip(10,10)
print(rect2.topleft) #(40,40)

rect1.union_ip(rect2)
print(rect1.width) #70

done=True
while done:
    events=pygame.event.get()
    for i in events:
        if i.type==pygame.QUIT:
            pygame.quit()
            done=False

