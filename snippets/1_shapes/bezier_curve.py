import cairo
import math

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)
    
    x0, y0 = 50, 50
    x1, y1 = 180, 220    
    x2, y2 = 350, 180
    x3, y3 = 400, 50
        
    c.move_to(x0, y0)
    c.curve_to(x1, y1, x2, y2, x3, y3)        
    c.stroke()
    
    for x,y in [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]:
        c.arc(x-2, y-2, 4, 0, 2*math.pi)
        c.stroke()
    
    surface.write_to_png(filename)
