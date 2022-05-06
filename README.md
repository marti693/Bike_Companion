# Bike_Companion
Tamagotchi style cycling companion

This link is a video demo for the project mounted on a bike working: https://drive.google.com/file/d/1VmsGMd6pqK_ocevbRaUjgUpMdF6Lu_CX/view?usp=sharing
This link is a video demo showcasing the functionality of taking care of the virtual pet: https://drive.google.com/file/d/1Vv4tPw2W0WMJExdbpOJT0YONV9SoFaQd/view?usp=sharing

Image_Shower.py is the python code that makes up the heart of the project. This version is made to be run on an IDE in Windows for testing.
images.zip contains all images used in the project. This file is necessary, and it must be able to be seen by the Image_Shower.py program.

A raspberry pi 2 was used for testing, and a raspberry pi zero was used as the final processor that runs all of the programs.

An ili9341 TFT display with touchscreen was used as the display.

The following GitHub project was used to display the images on the TFT at a fast framerate: https://github.com/juj/fbcp-ili9341. 

The following GitHub project was used to read the touchscreen: https://github.com/BehindTheSciences/ili9341_SPI_TouchScreen_LCD_Raspberry-Pi. lib_tft24T.py is used in the final design, and BTS-ili9341-touch-calibration.py was used as a reference of how to read the touch inputs. 

A Hall Effect Sensor was used to read when a rotation of the wheel occurs.

The following Pinout was used to connect the TFT display:

ili9341 Pin -	Raspberry Pi Pin
 * Vcc 		   - 3V3 Vcc
 * GND 		   - GND
 * CS 		   - GPIO26 (CE0)
 * Reset 		 - GPIO25
 * DC 		   - GPIO24
 * SDI(MOSI) -	MOSI (SPI0)
 * SCLK 		 - SPI0 SCLK
 * LED 		   - GPIO18
 * SDO(MISO) -	SPI0 MISO
 * T_clk 		 - SPI1 SCLK 	/ GPIO21
 * T_cs 		 - SPI1 CE0	/ GPIO16 
 * T_DIN 		 - SPI1 MOSI	/ GPIO20
 * T_DO 		 - SPI1 MISO	/ GPIO19
 * T_IRQ 		 - GPIO26

