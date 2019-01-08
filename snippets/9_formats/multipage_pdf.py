import cairo
from cairo import PDFSurface
import math

def draw_pdf(filename):
    
    surface = PDFSurface(filename, 320, 240)
    c = cairo.Context(surface)

    c.set_source_rgb(1, 1, 1)
    c.paint()

    c.arc(150, 150, 50, 0, 2*math.pi)
    c.set_source_rgba(1,0,0,1)
    c.fill()

    surface.show_page()

    c.set_source_rgb(1, 1, 1)
    c.paint()

    c.arc(100, 100, 50, 0, 2*math.pi)
    c.set_source_rgba(1,0,1,1)
    c.fill()

    surface.show_page()
