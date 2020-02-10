#!/usr/bin/env python
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if(x0 > x1):
        temp = x1
        x1 = x0
        x0 = temp
        temp = y1
        y1 = y0
        y0 = temp
    #print(x0, y0, x1, y1)
    if(x1 == x0): slope = 5
    elif(y0 == y1): slope = 0
    else: slope = (y1-y0)/(x1-x0)
    if(slope > 0):
        if(slope <= 1): octant1( x0, y0, x1, y1, screen, color)
        else: octant2( x0, y0, x1, y1, screen, color)
    else:
        if(slope >= -1): octant8( x0, y0, x1, y1, screen, color)
        else: octant7( x0, y0, x1, y1, screen, color)
        
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
   
def octant7(x0, y0, x1, y1, screen, color):
    A = (y1-y0)
    B = 2*(x0-x1)
    d = A - B
    while( y0 >= y1):
        plot(screen, color, x0, y0)
        if(d > 0):
            x0 = x0+1
            d = d + 2*A
        y0 = y0-1
        d = d - B

def octant8(x0, y0, x1, y1, screen, color):
    A = 2*(y1-y0)
    B = (x0-x1)
    d = A - B
    while( x0 <= x1):
        plot(screen, color, x0, y0)
        if(d < 0):
            y0 = y0-1
            d = d - 2*B
        x0 = x0+1
        d = d + A
