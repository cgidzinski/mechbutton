import os
import time
from time import sleep
from threading import Thread
from neopixel import *
import argparse
import RPi.GPIO as GPIO

# LED strip configuration:
SW_PIN         = 13
LED_COUNT      = 5      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
trigger = 0
def colorWipe(strip, color, wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def sound():
	os.system('mpg123 http://ice1.somafm.com/u80s-128-mp3')

def rainbow(strip):
	for x in range(10):
		for pos in range(5):
			strip.setPixelColorRGB(pos, 0, 0, 255)
		strip.show()
		time.sleep(100)
		for pos in range(5):
			strip.setPixelColorRGB(pos, 0,255,0)
		strip.show()
		time.sleep(100)
		for pos in range(5):
			strip.setPixelColorRGB(pos, 255,0,0)
		strip.show()
		time.sleep(100)

def standby(strip):
	for pos in range(5):
		strip.setPixelColorRGB(pos, 0, 0, 255)
	strip.show()

# Main program logic follows:
if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SW_PIN, GPIO.IN)
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()
	try:
		while True:
			if (GPIO.input(SW_PIN)== False):
				print "Button"	
				rainbow(strip)			
			standby(strip)


	except KeyboardInterrupt:
			colorWipe(strip, Color(0,0,0), 10)
