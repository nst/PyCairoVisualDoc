import cairo
import math

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 320, 240)
    c = cairo.Context(surface)

    c.set_source_rgb(1, 1, 1)
    c.paint()

    c.arc(100, 80, 50, 0, 2*math.pi)
    c.set_source_rgba(1,0,0,1)
    c.fill()
    
    surface.write_to_png(filename)
