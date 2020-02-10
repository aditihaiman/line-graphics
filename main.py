#!/usr/bin/env python
from display import *
from draw import *
import random
import math

s = new_screen()
c = [ 0, 255, 0 ]


##-------------------------------TESTING------------------------------##


##octants 1 and 5
#draw_line(0, 0, XRES-1, YRES-1, s, c) #(0,0) - (499, 499)
#draw_line(0, 0, XRES-1, YRES / 2, s, c) #(0,0) - (499, 250)
#draw_line(XRES-1, YRES-1, 0, 250, s, c) #(499, 499) - (0, 250)
#
##octants 8 and 4
#c[BLUE] = 255;
#draw_line(0, YRES-1, XRES-1, 0, s, c); #(0, 499) - (499, 0)
#draw_line(0, YRES-1, XRES-1, YRES/2, s, c); #(0, 499) - (499, 250)
#draw_line(XRES-1, 0, 0, 250, s, c); #(499, 0) - (0, 250)
#
##octants 2 and 6
#c[RED] = 255;
#c[GREEN] = 0;
#c[BLUE] = 0;
#draw_line(0, 0, 250, YRES-1, s, c); #(0,0) - (250, 499)
#draw_line(XRES-1, YRES-1, 250, 0, s, c); #(499,499) - (250, 0)
#draw_line(250, 499, 499, 0, s, c);
#
##octants 7 and 3
#c[BLUE] = 255;
#draw_line(0, YRES-1, 250, 0, s, c); #(0, 499) - (250, 0)
#draw_line(XRES-1, 0, 250, YRES-1, s, c); #(499, 0) - (250, 499)
#
##horizontal and vertical
#c[BLUE] = 0;
#c[GREEN] = 255;
#draw_line(0, 250, 499, 250, s, c); #horizontal
#draw_line(250, 0, 250, 499, s, c); #vertical

##-----------------------EL GIRAFFO---------------------------##

#c[RED] = 255;
#c[BLUE] = 0;
#c[GREEN] = 255;
#
##draw_line(100, 0, 250, 500, s, c);
##draw_line(250, 500, 400, 0, s, c);
##draw_line(400, 0, 0, 300, s, c);
##draw_line(0, 300, 500, 300, s, c);
##draw_line(500, 300, 100, 00, s, c);
#
##body
#draw_line(200, 50, 350, 50, s, c);
#draw_line(250, 125, 350, 125, s, c);
#draw_line(350, 50, 350, 125, s, c);
#
##neck
#draw_line(200, 50, 200, 350, s, c);
#draw_line(250, 125, 250, 410, s, c);
#
##face
#draw_line(200, 350, 150, 300, s, c);
#draw_line(200, 350, 150, 300, s, c);
#draw_line(150, 300, 120, 330, s, c);
#draw_line(120, 330, 200, 410, s, c);
#draw_line(200, 410, 250, 410, s, c);
#draw_line(140, 310, 175, 345, s, c);
#
##ears
#draw_line(238, 440, 250, 440, s, c);
#draw_line(215, 440, 227, 440, s, c);
#draw_line(238, 410, 238, 440, s, c);
#draw_line(250, 410, 250, 440, s, c);
#draw_line(215, 410, 215, 440, s, c);
#draw_line(227, 410, 227, 440, s, c);
#
##eye
#draw_line(215, 380, 225, 380, s, c);
#draw_line(215, 380, 215, 390, s, c);
#draw_line(215, 390, 225, 390, s, c);
#draw_line(225, 380, 225, 390, s, c);
#
##legs
#draw_line(215, 1, 225, 1, s, c);
#draw_line(215, 10, 215, 50, s, c);
#draw_line(225, 1, 225, 50, s, c);
#draw_line(215, 1, 200, 1, s, c);
#draw_line(200, 1, 200, 10, s, c);
#draw_line(200, 10, 215, 10, s, c);
#draw_line(330, 1, 340, 1, s, c);
#draw_line(330, 10, 330, 50, s, c);
#draw_line(340, 1, 340, 50, s, c);
#draw_line(330, 1, 315, 1, s, c);
#draw_line(315, 1, 315, 10, s, c);
#draw_line(315, 10, 330, 10, s, c);
#draw_line(200, 6, 210, 6, s, c);
#draw_line(315, 6, 325, 6, s, c);
#
##tail
#draw_line(350, 125, 370, 160, s, c);
#
##sun
#draw_line(0, 400, 75, 425, s, c);
#draw_line(75, 425, 100, 499, s, c);
#draw_line(37, 413, 62, 325, s, c);
#draw_line(75, 425, 130, 370, s, c);
#draw_line(87, 457, 175, 432, s, c);
#
##border and tree
#c[RED] = 0;
#draw_line(0, 0, 500, 0, s, c);
#draw_line(100, 105, 70, 175, s, c);
#draw_line(100, 105, 100, 200, s, c);
#draw_line(100, 105, 130, 175, s, c);
#c[GREEN] = 0;
#c[BLUE] = 255;
#draw_line(0, 0, 0, 500, s, c);
#draw_line(0, 499, 499, 499, s, c);
#draw_line(499, 0, 499, 499, s, c);
#c[RED] = 150;
#c[GREEN] = 75;
#c[BLUE] = 0;
#draw_line(100, 0, 100, 105, s, c);
#
#def drawSpot(x0, y0, side, s, c):
#    draw_line(x0, y0, x0+side, y0, s, c);
#    draw_line(x0, y0, x0, y0+side, s, c);
#    draw_line(x0+side, y0, x0+side, y0+side, s, c);
#    draw_line(x0+side, y0+side, x0, y0+side, s, c);
#
##spots
#drawSpot(210, 70, 10, s, c);
#drawSpot(230, 90, 10, s, c);
#drawSpot(213, 110, 10, s, c);
#drawSpot(222, 130, 10, s, c);
#drawSpot(233, 150, 10, s, c);
#drawSpot(211, 170, 10, s, c);
#drawSpot(228, 190, 10, s, c);
#drawSpot(214, 210, 10, s, c);
#drawSpot(231, 230, 10, s, c);
#drawSpot(225, 250, 10, s, c);
#drawSpot(213, 270, 10, s, c);
#drawSpot(234, 290, 10, s, c);
#drawSpot(216, 310, 10, s, c);
#drawSpot(226, 330, 10, s, c);
#drawSpot(250, 66, 10, s, c);
#drawSpot(270, 101, 10, s, c);
#drawSpot(290, 72, 10, s, c);
#drawSpot(310, 93, 10, s, c);
#drawSpot(330, 110, 10, s, c);
#drawSpot(330, 65, 10, s, c);
#
##clouds
#c[RED] = 255;
#c[BLUE] = 255;
#c[GREEN] = 255;
#draw_line(50, 305, 110, 305, s, c);
#draw_line(50, 285, 50, 305, s, c);
#draw_line(50, 285, 50, 305, s, c);
#draw_line(50, 285, 25, 285, s, c);
#draw_line(25, 260, 25, 285, s, c);
#draw_line(25, 260, 40, 260, s, c);
#draw_line(40, 260, 70, 260, s, c);
#draw_line(70, 245, 70, 260, s, c);
#draw_line(70, 245, 120, 245, s, c);
#draw_line(120, 245, 120, 270, s, c);
#draw_line(120, 270, 135, 270, s, c);
#draw_line(135, 270, 135, 290, s, c);
#draw_line(135, 290, 110, 290, s, c);
#draw_line(110, 290, 110, 305, s, c);
#
#draw_line(50+300, 305+40, 110+300, 305+40, s, c);
#draw_line(50+300, 285+40, 50+300, 305+40, s, c);
#draw_line(50+300, 285+40, 50+300, 305+40, s, c);
#draw_line(50+300, 285+40, 25+300, 285+40, s, c);
#draw_line(25+300, 260+40, 25+300, 285+40, s, c);
#draw_line(25+300, 260+40, 40+300, 260+40, s, c);
#draw_line(40+300, 260+40, 70+300, 260+40, s, c);
#draw_line(70+300, 245+40, 70+300, 260+40, s, c);
#draw_line(70+300, 245+40, 120+300, 245+40, s, c);
#draw_line(120+300, 245+40, 120+300, 270+40, s, c);
#draw_line(120+300, 270+40, 135+300, 270+40, s, c);
#draw_line(135+300, 270+40, 135+300, 290+40, s, c);
#draw_line(135+300, 290+40, 110+300, 290+40, s, c);
#draw_line(110+300, 290+40, 110+300, 305+40, s, c);

##---------------------------OTHER STUFF---------------------------##

for x in range(100):
    x0 = x
    y0 = x
    x1 = abs(int(math.sin(x)*500))
    y1 = abs(int(math.cos(x)*500))
    draw_line(x0, y0, x1, y1, s, c);
    c[2] += 2

c = [ 0, 0, 255 ]

for x in range(100):
    x0 = 500-x
    y0 = 500-x
    x1 = abs(int(math.sin(x)*500))
    y1 = abs(int(math.cos(x)*500))
    draw_line(x0, y0, x1, y1, s, c);
    c[0] += 2

c = [ 255, 0, 0 ]

for x in range(100):
    x0 = 500-x
    y0 = x
    x1 = abs(int(math.sin(x)*500))
    y1 = abs(int(math.cos(x)*500))
    draw_line(x0, y0, x1, y1, s, c);
    c[1] += 2

c = [ 255, 0, 0 ]

for x in range(100):
    x0 = x
    y0 = 500-x
    x1 = abs(int(math.sin(x)*500))
    y1 = abs(int(math.cos(x)*500))
    draw_line(x0, y0, x1, y1, s, c);
    c[1] += 2
    


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
