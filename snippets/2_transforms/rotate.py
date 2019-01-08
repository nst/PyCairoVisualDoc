import cairo
import math

def draw_png_rotate(filename):

    surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, 512, 300)
    c = cairo.Context(surface)
    
    c.set_source_rgb(1,1,1)
    c.paint()
    
    c.set_source_rgb(0,0,0)
    
    c.save()
    c.translate(50, 50)
    c.rectangle(0, 0, 250, 150)
    c.stroke()
    c.restore()
    
    c.save()
    c.translate(250, 150)
    c.rotate(math.pi / 4.0)
    c.rectangle(0, 0, 250, 150)
    c.stroke()
    c.restore()
    
    surface.write_to_png(filename)
