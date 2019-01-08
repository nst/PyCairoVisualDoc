import cairo
import math

def draw_rect(c):
    c.set_source_rgb(1,0,0)
    c.rectangle(20, 20, 150, 100)
    c.fill()

def draw_png_asd(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)
    
    draw_rect(c)
    
    # x_new = xx * x + xy * y + x0
    # y_new = yx * x + yy * y + y0

    # cairo.Matrix(xx, yx,
    #              xy, yy,
    #              x0, y0)
    
    m = cairo.Matrix(1.0, 0.5,
                     0,   1.0,
                     256, 0.0)
    
    c.transform(m)
    
    draw_rect(c)
    
    surface.write_to_png(filename)
