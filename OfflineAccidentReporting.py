import RPi.GPIO as GPIO
import pygame
import sys
import time
from pygame import gfxdraw

print "Launching Accident Reporting Service..."

time.sleep(2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN) #Warning
GPIO.setup(20, GPIO.IN) #EStop

pygame.init()
pygame.font.init()

title='Accident/ Near-Miss Incident Reporting Dashboard'
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

warningMessage1 = messageFont.render("Safe, no intruders.                    ", True, (255,255,255), background)
warningMessage2 = messageFont.render("Intruder Detected!    ", True, (255,255,255), background)
machineMessage1 = messageFont.render("Machine Running.      ", True, (255,255,255), background)
machineMessage2 = messageFont.render("Machine Stopped!", True, (255,255,255), background)

screen.fill(background)
safe = (0,255,0)
dangerous = (255,0,0)

def warningStatus(color):
	pygame.gfxdraw.filled_circle(screen, 400, 256, 120, color)
	pygame.gfxdraw.aacircle(screen, 400, 256, 120, color)	

def estopStatus(color):
        pygame.gfxdraw.filled_circle(screen, 930, 256, 120, color)
	pygame.gfxdraw.aacircle(screen, 930, 256, 120, color)	


while True:
	
	#Poll Current GPIO Status
	Warning_status = GPIO.input(16)
	Estop_status = GPIO.input(20)
	
	if Warning_status==1:
		warningStatus(dangerous)
		screen.blit(warningMessage2, (260,400))
	elif Warning_status==0:
		warningStatus(safe)
		screen.blit(warningMessage1, (260,400))
		
	if Estop_status==1:
		estopStatus(dangerous)
		screen.blit(machineMessage2, (800,400))
	elif Estop_status==0:
		estopStatus(safe)
		screen.blit(machineMessage1, (800,400))

	screen.blit(img,(1250,650))
	pygame.display.flip()
	
	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
                   pygame.quit(); sys.exit();
