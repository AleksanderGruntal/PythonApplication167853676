import pygame,sys
pygame.init()
#värvid
kollane=[255,255,10]
punane=[255,0,0]
hall=[255,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("xd.png")
posX=X-mesilane.get_rect().width
posY=Y-mesilane.get_rect().height
lõpp=False
samm=2

while not lõpp:
    kell.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
         sys.exit()
    if posX==0 and posY==0:
        sammX=1
        sammY=0
    if posX==X-mesilane.get_rect().width and posY<=Y-mesilane.get_rect().height:
        sammX=0
        sammY=1
    if posX<=X-mesilane.get_rect().width and posY==Y-mesilane.get_rect().height:
        sammX=1
        sammY=0
        sammX=-sammX
    if posX==0 and posY>=Y-mesilane.get_rect().height:
        sammX=0
        sammY=1
        sammY=-sammY
    posX+=sammX
    posY+=sammY
    ekraan.blit(mesilane,(posX,posY))
    pygame.display.flip()
    ekraan.fill(roheline)

pygame.quit()

# номер 1
#    if posX <= 1:
#        posX = 0
#       posY -= samm
#
#    if posY <= 435:
#        posY = 0
#        posX += samm + 2
#
#    if posX >= X - mesilane.get_rect().width:
#        posX = X - mesilane.get_rect().width
#        posY += samm
#
#    if posY >= Y - mesilane.get_rect().height:
#        posY = Y - mesilane.get_rect().height
#        posX -= samm + 2

# номер 2
#    if posX <= 0:
#        posX = 0
#        posY -= samm
#
#    if posY <= 0:
#        posY = 0
#        posX += samm + 2
#
#   if posX >= X - mesilane.get_rect().width:
#       posX = X - mesilane.get_rect().width
#        posY += samm
#
#    if posY >= Y - mesilane.get_rect().height:
#        posY = Y - mesilane.get_rect().height
#        posX -= samm + 2

# номер 3
#    if posX==0 and posY==0:
#        sammX=1
#        sammY=0
#    if posX==X-mesilane.get_rect().width and posY<=Y-mesilane.get_rect().height:
#        sammX=0
#        sammY=1
#    if posX<=X-mesilane.get_rect().width and posY==Y-mesilane.get_rect().height:
#        sammX=1
#        sammY=0
#        sammX=-sammX
#    if posX==0 and posY>=Y-mesilane.get_rect().height:
#        sammX=0
#        sammY=1
#        sammY=-sammY
#    posX+=sammX
#    posY+=sammY
#    ekraan.blit(mesilane,(posX,posY))
#    pygame.display.flip()
#    ekraan.fill(roheline)
