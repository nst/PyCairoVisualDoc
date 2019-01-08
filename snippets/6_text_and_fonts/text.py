#!/usr/bin/env python

import cairo

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)

    # choose font
        
    c.select_font_face("Courier New")
    c.set_font_size(14)

    # basic example

    c.move_to(50, 50)
    c.show_text("Hello World")

    # right align

    for y, adj in [(100, "naughty"), (120, "cool"), (140, "bad")]:
        s = "%s cats" % adj
        _, _, txt_width, _, _, _ = c.text_extents(s)        
        c.move_to(150 - txt_width, y)
        c.show_text(s)
    
    # pick another font
       
    c.select_font_face("Times",
                       cairo.FONT_SLANT_ITALIC,
                       cairo.FONT_WEIGHT_BOLD)
    c.set_font_size(56)

    c.move_to(200, 100)
    c.show_text("Hi there")

    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_gif_sqlogo("x.gif")
