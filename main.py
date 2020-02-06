#!/usr/bin/env python
from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c) #(0,0) - (499, 499)
draw_line(0, 0, XRES-1, YRES / 2, s, c) #(0,0) - (499, 250)
draw_line(XRES-1, YRES-1, 0, 250, s, c) #(499, 499) - (0, 250)

#octants 8 and 4
c[BLUE] = 255;
draw_line(0, YRES-1, XRES-1, 0, s, c); #(0, 499) - (499, 0)
draw_line(0, YRES-1, XRES-1, YRES/2, s, c); #(0, 499) - (499, 250)
draw_line(XRES-1, 0, 0, 250, s, c); #(499, 0) - (0, 250)

#octants 2 and 6
c[RED] = 255;
c[GREEN] = 0;
c[BLUE] = 0;
draw_line(0, 0, 250, YRES-1, s, c); #(0,0) - (250, 499)
draw_line(XRES-1, YRES-1, 250, 0, s, c); #(499,499) - (250, 0)
#draw_line(250, 499, 499, 0, s, c);

#octants 7 and 3
c[BLUE] = 255;
draw_line(0, YRES-1, 250, 0, s, c); #(0, 499) - (250, 0)
draw_line(XRES-1, 0, 250, YRES-1, s, c);

#horizontal and vertical
c[BLUE] = 0;
c[GREEN] = 255;
draw_line(0, 250, 499, 250, s, c);
draw_line(250, 0, 250, 499, s, c);

#
#draw_line(0, 0, 500, 100, s, c); #octant 1
#draw_line(0, 0, 100, 500, s, c); #octant 2
#draw_line(0, 0, 500, 0, s, c); #octant 1
#draw_line(0, 500, 500, 300, s, c); #octant 8
#draw_line(0, 500, 300, 0, s, c); #octant 7
##draw_line(0, 500, 500, 500, s, c);

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
