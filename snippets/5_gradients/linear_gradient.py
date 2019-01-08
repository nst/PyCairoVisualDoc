#!/usr/bin/env python

import cairo
import math

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)
    
    x0, y0 = 20, 20
    x1, y1 = 20, 220
    lg = cairo.LinearGradient(x0, y0, x1, y1)
    lg.add_color_stop_rgba(0.0, 1, 0, 0, 1) 
    lg.add_color_stop_rgba(0.5, 0, 1, 0, 1) 
    lg.add_color_stop_rgba(1.0, 0, 0, 1, 1) 

    c.rectangle(20, 20, 200, 200)
    c.set_source(lg)
    c.fill()
    
    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_png("x.gif")
