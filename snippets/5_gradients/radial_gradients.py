#!/usr/bin/env python

import cairo
import math

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)
    
    # cx0 - x coordinate for the center of the start circle
    # cy0 - y coordinate for the center of the start circle
    # radius0 - radius of the start circle
    # cx1 - x coordinate for the center of the end circle
    # cy1 - y coordinate for the center of the end circle
    # radius1 - radius of the end circle

    pat = cairo.RadialGradient(135, 130, 15,
                               140, 140, 40)
    pat.add_color_stop_rgba(0, 1, 1, 1, 1)
    pat.add_color_stop_rgba(0.3, 0.5, 0.5, 1, 1)
    pat.add_color_stop_rgba(1, 0, 0, 1, 1)
    c.set_source(pat)
    c.arc(150, 150, 50, 0, 2*math.pi)
    c.fill()
    
    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_png("radial_gradient.png")
