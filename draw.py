#!/usr/bin/env python
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    print(x0, y0, x1, y1)
    if(x0 == x1): slope = 0
    else: slope = (y1-y0)/(x1-x0)
    if(slope > 0):
        if(slope <= 1): octant1( x0, y0, x1, y1, screen, color)
        else: octant2( x0, y0, x1, y1, screen, color)
        
def octant1( x0, y0, x1, y1, screen, color ):
    A = 2*(y1-y0)
    B = (x0-x1)
    d = A + B
    while( x0 <= x1):
        plot(screen, color, x0, y0)
        if(d > 0):
            y0 = y0+1
            d = d + 2*B
        x0 = x0+1
        d = d + A

def octant2(x0, y0, x1, y1, screen, color):
    A = (y1-y0)
    B = 2*(x0-x1)
    d = A + B
    while (y0 <= y1):
        plot(screen, color, x0, y0)
        if(d<0):
            x0 = x0 + 1
            d = d + 2*A
        y0 = y0 + 1
        d = d + B