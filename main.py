import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 1      # Number of LED pixels.
LED_PIN        = 10      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def colorWipe(strip, color, wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
time.sleep(wait_ms/1000.0)

def rainbow(strip, wait_ms=20, iterations=1):
	pos = 0
	strip.setPixelColorRGB(pos, 0, 0, 255)
	strip.show()
	time.sleep(wait_ms/1000.0)
	strip.setPixelColorRGB(pos, 0,255,0)
	strip.show()
	time.sleep(wait_ms/1000.0)
	strip.setPixelColorRGB(pos, 255,0,0)
	strip.show()
	time.sleep(wait_ms/1000.0)



# Main program logic follows:
if __name__ == '__main__':


	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()

	try:
		while True:
 
			rainbow(strip)


	except KeyboardInterrupt:
			colorWipe(strip, Color(0,0,0), 10)
