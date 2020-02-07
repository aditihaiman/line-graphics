#!/usr/bin/env python
from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

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
c[RED] = 255;
c[BLUE] = 0;
c[GREEN] = 255;

#draw_line(100, 0, 250, 500, s, c);
#draw_line(250, 500, 400, 0, s, c);
#draw_line(400, 0, 0, 300, s, c);
#draw_line(0, 300, 500, 300, s, c);
#draw_line(500, 300, 100, 00, s, c);

#body
draw_line(200, 50, 350, 50, s, c);
draw_line(250, 125, 350, 125, s, c);
draw_line(350, 50, 350, 125, s, c);

#neck
draw_line(200, 50, 200, 350, s, c);
draw_line(250, 125, 250, 410, s, c);

#face
draw_line(200, 350, 150, 300, s, c);
draw_line(200, 350, 150, 300, s, c);
draw_line(150, 300, 120, 330, s, c);
draw_line(120, 330, 200, 410, s, c);
draw_line(200, 410, 250, 410, s, c);

#ears
draw_line(238, 440, 250, 440, s, c);
draw_line(215, 440, 227, 440, s, c);
draw_line(238, 410, 238, 440, s, c);
draw_line(250, 410, 250, 440, s, c);
draw_line(215, 410, 215, 440, s, c);
draw_line(227, 410, 227, 440, s, c);

#eye
draw_line(215, 380, 225, 380, s, c);
draw_line(215, 380, 215, 390, s, c);
draw_line(215, 390, 225, 390, s, c);
draw_line(225, 380, 225, 390, s, c);

#legs
draw_line(215, 1, 225, 1, s, c);
draw_line(215, 10, 215, 50, s, c);
draw_line(225, 1, 225, 50, s, c);
draw_line(215, 1, 200, 1, s, c);
draw_line(200, 1, 200, 10, s, c);
draw_line(200, 10, 215, 10, s, c);
draw_line(330, 1, 340, 1, s, c);
draw_line(330, 10, 330, 50, s, c);
draw_line(340, 1, 340, 50, s, c);
draw_line(330, 1, 315, 1, s, c);
draw_line(315, 1, 315, 10, s, c);
draw_line(315, 10, 330, 10, s, c);

#tail
draw_line(350, 125, 370, 160, s, c);

#border and tree
c[RED] = 0;
draw_line(0, 0, 500, 0, s, c);
draw_line(100, 105, 70, 175, s, c);
draw_line(100, 105, 100, 200, s, c);
draw_line(100, 105, 130, 175, s, c);
c[GREEN] = 0;
c[BLUE] = 255;
draw_line(0, 0, 0, 500, s, c);
draw_line(0, 499, 499, 499, s, c);
draw_line(499, 0, 499, 499, s, c);
c[RED] = 150;
c[GREEN] = 75;
c[BLUE] = 0;
draw_line(100, 0, 100, 105, s, c);



display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
