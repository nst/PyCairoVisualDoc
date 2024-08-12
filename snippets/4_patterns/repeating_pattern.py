#!/usr/bin/env python

import cairo
import math
import os

def create_from_png(image_name):
    # ensure we can read image when working from another dir
    cwd = os.getcwd()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    ims = cairo.ImageSurface.create_from_png(image_name)
    os.chdir(cwd)
    return ims

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)
    
    # pattern surface
    ps = cairo.ImageSurface(cairo.FORMAT_ARGB32, 50, 50)
    pc = cairo.Context(ps)
    
    # draw blue circles on the pattern surface context
    pc.set_source_rgb(1, 1, 1)
    pc.paint()
    pc.set_source_rgb(0, 0, 1)
    pc.arc(25, 25, 10, 0, 2 * 3.14159)
    pc.fill()

    # create the pattern
    p = cairo.SurfacePattern(ps)
    p.set_extend(cairo.EXTEND_REPEAT)

    # Use the pattern to fill the main surface
    c.set_source(p)
    c.rectangle(100, 50, 300, 200)
    c.fill()
    
    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_png("repeating_pattern.png")
