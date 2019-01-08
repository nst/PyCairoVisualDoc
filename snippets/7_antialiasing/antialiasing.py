#!/usr/bin/env python

import cairo
import math

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)
    
    c.select_font_face("Courier New")
    c.set_font_size(28)

    fo = cairo.FontOptions()
    fo.set_antialias(cairo.ANTIALIAS_DEFAULT)
    c.set_font_options(fo)

    c.move_to(50, 50)
    c.show_text("Antialias Default")    

    fo = cairo.FontOptions()
    fo.set_antialias(cairo.ANTIALIAS_NONE)
    c.set_font_options(fo)

    c.move_to(50, 100)
    c.show_text("Antialias None")    

    #
    
    c.set_antialias(cairo.ANTIALIAS_DEFAULT)

    c.arc(170, 170, 50, 0, 2*math.pi)
    c.set_source_rgba(1,0,0,1)
    c.fill()

    c.set_antialias(cairo.ANTIALIAS_NONE)

    c.arc(370, 170, 50, 0, 2*math.pi)
    c.set_source_rgba(1,0,0,1)
    c.fill()
    
    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_png("x.gif")
