import cairo
import math

def draw_picture(c, x, y, scale):

    c.save()
    
    c.translate(x, y)
    c.scale(scale, scale)

    c.set_source_rgb(1, 0, 0)
    c.arc(120, 120, 120, 0, 2*math.pi)
    c.fill()

    c.set_source_rgb(1, 1, 1)
    c.arc(160, 90, 40, 0, 2*math.pi)
    c.fill()
        
    c.restore()

def draw_png_asd(filename):

    surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, 512, 300)
    #surface.set_device_scale(2,2)
    c = cairo.Context(surface)
    #c.set_antialias(cairo.ANTIALIAS_NONE)
    
    c.set_source_rgb(1, 1, 1)
    c.paint()
    
    draw_picture(c, x=30, y=30, scale=1)
    draw_picture(c, x=350, y=50, scale=0.5)
    draw_picture(c, x=290, y=170, scale=0.25)
    
    surface.write_to_png(filename)
