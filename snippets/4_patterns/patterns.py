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
    
    pat_surface = create_from_png("brick.png")
    pat = cairo.SurfacePattern(pat_surface)
    pat.set_extend(cairo.EXTEND_REPEAT)
    
    c.set_source(pat)
    c.arc(100, 100, 50, 0, 2*math.pi)
    c.fill()
    
    c.set_source_surface(pat_surface, 256, 50)    
    c.paint()

    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_gif_sqlogo("brick.png")
