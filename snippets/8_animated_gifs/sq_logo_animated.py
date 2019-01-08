#!/usr/bin/env python

import cairo
import math
import imageio
import numpy

from PIL import Image

COLOR_ORANGE_SQ = (250/255., 92/255., 53/255.)
COLOR_WHITE = (1, 1, 1)

def as_numpy_array(surface):

    w = surface.get_width()
    h = surface.get_height()
    
    data = surface.get_data()
    
    a = numpy.ndarray(shape=(h,w), dtype=numpy.uint32, buffer=data)
    
    i = Image.frombytes("RGBA", (w,h), a, "raw", "BGRA", 0, 1)
    
    return numpy.asarray(i)

def add_image(writer, surface):
    
    a = as_numpy_array(surface)
    writer.append_data(a)
    
def draw_gif_sqlogo(filename):

    gif_writer = imageio.get_writer(filename, mode='I', duration=0.5)
        
    w, h = 280, 280
    
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    c = cairo.Context(surface)
    
    # white background
    
    c.set_source_rgb(1, 1, 1)
    c.paint()
    c.fill()
    #add_image(gif_writer, surface)
    
    c.translate(20, 20)

    # main circle
    
    c.set_source_rgb (*COLOR_ORANGE_SQ)
    c.arc(120, 120, 120, 0, 2*math.pi)
    c.fill()
    add_image(gif_writer, surface)
    
    # white rects
    
    c.set_source_rgb (*COLOR_WHITE)
    c.rectangle(60, 70, 120, 20)
    c.fill()
    add_image(gif_writer, surface)

    c.rectangle(60, 110, 120, 60)
    c.fill()
    add_image(gif_writer, surface)
    
    # orange part of the bridge
    
    c.set_source_rgb (*COLOR_ORANGE_SQ)
    c.rectangle(80, 145, 30, 25)
    c.fill()
    add_image(gif_writer, surface)
    
    c.rectangle(130, 145, 30, 25)
    c.fill()
    add_image(gif_writer, surface)

    c.arc(95, 145,  15, 0, 2*math.pi)
    c.fill()
    add_image(gif_writer, surface)

    c.arc(145, 145, 15, 0, 2*math.pi)
    c.fill()
    add_image(gif_writer, surface)

if __name__ == "__main__":

    draw_gif_sqlogo("sq.gif")
