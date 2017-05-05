import RPi.GPIO as GPIO
import pygame
import sys
import time
from pygame import gfxdraw

print "Launching Smart Car Park Dashboard..."

time.sleep(2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) #Car Park 1
GPIO.setup(27, GPIO.IN) #Car Park 2
GPIO.setup(22, GPIO.IN) #Route 1
GPIO.setup(5, GPIO.IN)  #Route 2
GPIO.setup(6, GPIO.IN)  #Route 3
GPIO.setup(13, GPIO.IN) #Rain

pygame.init()
pygame.font.init()

title='Smart Car Park Dashboard'
screen = pygame.display.set_mode((1363,768),pygame.RESIZABLE|pygame.DOUBLEBUF,32)
background = (6,6,6)
titleFont = "./TT0248M_.TTF"
titleSize = 30
messageFont = "./TT0248M_.TTF"
messageSize = 45
messageFont = pygame.font.Font(messageFont, messageSize)
myfont = pygame.font.Font(titleFont, titleSize)
pygame.display.set_caption(title)
img = pygame.image.load('white logo small.jpg')

parkingNotification = myfont.render("Park In:",True,(255,255,255), background)
routeNotification = myfont.render("Take Route:",True,(255,255,255), background)

parkingMessage1 = messageFont.render("Go to Parking Lot A.                                                  ", True, (255,255,255), background)
parkingMessage2 = messageFont.render("Go to Parking Lot B.                                                  ", True, (255,255,255), background)
parkingMessage3 = messageFont.render("Both parking lots full. Consider using public transport.", True, (255,255,255), background)

routeMessage1 = messageFont.render("Go via Route 1.   ", True, (255,255,255), background)
routeMessage2 = messageFont.render("Go via Route 2.   ", True, (255,255,255), background)
routeMessage3 = messageFont.render("Go via Toll-Route.", True, (255,255,255), background)

weatherMessage1 = messageFont.render("The weather is bright and sunny. Have a good day!", True, (255,255,255), background)
weatherMessage2 = messageFont.render("Rainfall is expected. Drive safely.                                   ", True, (255,255,255), background)

screen.fill(background)
available = (247,143,30)
unavailable = (255,255,255)
dry = (255,255,255)
rainy = (0,200,255)

def parkAStatus(color):
	pygame.gfxdraw.filled_circle(screen, 170, 150, 80, color)
	pygame.gfxdraw.aacircle(screen, 170, 150, 80, color)	
	parkALabel = myfont.render("Park A",True,(255,255,255), background)
        screen.blit(parkALabel, (120,270))

def parkBStatus(color):
        pygame.gfxdraw.filled_circle(screen, 380, 150, 80, color)
	pygame.gfxdraw.aacircle(screen, 380, 150, 80, color)	
	parkBLabel = myfont.render("Park B",True, (255,255,255),background)
        screen.blit(parkBLabel, (370,270))

def route1Status(color):
        pygame.gfxdraw.filled_circle(screen, 720, 150, 80, color)
	pygame.gfxdraw.aacircle(screen, 720, 150, 80, color)	
	route1Label = myfont.render("Route 1",True,(255,255,255),background)
        screen.blit(route1Label, (680,270))

def route2Status(color):
        pygame.gfxdraw.filled_circle(screen, 950, 150, 80, color)
	pygame.gfxdraw.aacircle(screen, 950, 150, 80, color)	
	route2Label = myfont.render("Route 2",True,(255,255,255),background)
        screen.blit(route2Label, (910,270))

def tollRouteStatus(color):
        pygame.gfxdraw.filled_circle(screen, 1180, 150, 80, color)
	pygame.gfxdraw.aacircle(screen, 1180, 150, 80, color)	
	tollRouteLabel = myfont.render("Toll Route",True,(255,255,255),background)
        screen.blit(tollRouteLabel, (1130,270))

def weatherStatus(color):
        pygame.gfxdraw.filled_circle(screen, 285, 450, 80, color)
	pygame.gfxdraw.aacircle(screen, 285, 450, 80, color)
	weatherLabel = myfont.render("Weather",True,(255,255,255),background)
        screen.blit(weatherLabel, (240,570))


while True:
	
	#Poll GPIO for current status
	ParkA_status = GPIO.input(17)
	ParkB_status = GPIO.input(27)
	Route1_status = GPIO.input(22)
	Route2_status = GPIO.input(5)
	TollRoute_status = GPIO.input(6)
	Weather_status = GPIO.input(13)
	
	#Set Parking Lot Status on Display
	if ParkA_status==1:
		parkAStatus(available)
		parkBStatus(unavailable)
		screen.blit(parkingMessage1, (480,400))
	elif ParkB_status==1:
		parkBStatus(available)
		parkAStatus(unavailable)
		screen.blit(parkingMessage2, (480,400))
	else:
		parkAStatus(unavailable)
		parkBStatus(unavailable)
		screen.blit(parkingMessage3, (480,400))
	
	#Set Route Status on Display
	if Route1_status==1:
		route1Status(available)
		route2Status(unavailable)
		tollRouteStatus(unavailable)
		screen.blit(routeMessage1, (480,470))
	elif Route2_status==1:
		route2Status(available)
		route1Status(unavailable)
		tollRouteStatus(unavailable)
		screen.blit(routeMessage2, (480,470))
	elif TollRoute_status==1:
		tollRouteStatus(available)
		route1Status(unavailable)
		route2Status(unavailable)
		screen.blit(routeMessage3, (480,470))
	
	#Set Weather Status on Display
	if Weather_status==1:
		weatherStatus(rainy)
		screen.blit(weatherMessage2, (480,540))
	elif Weather_status==0:
		weatherStatus(dry)
		screen.blit(weatherMessage1, (480,540))
	
	#Update Text Message on Display
	screen.blit(img,(1250,650))
	screen.blit(parkingNotification, (220,10))
	screen.blit(routeNotification, (890,10))
	pygame.display.flip()
 
	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
                   pygame.quit(); sys.exit();
