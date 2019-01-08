import cairo
from cairo import SVGSurface
import math

def draw_svg_asd(filename):
    
    surface = SVGSurface(filename, 320, 240)
    c = cairo.Context(surface)

    c.set_source_rgb(1, 1, 1)
    c.paint()

    c.arc(100, 80, 50, 0, 2*math.pi)
    c.set_source_rgba(1,0,0,1)
    c.fill()

    surface.finish()
