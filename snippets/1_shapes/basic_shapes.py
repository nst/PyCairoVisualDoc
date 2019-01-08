import cairo
import math

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)
    
    # background
    c.set_source_rgb(1,1,1)
    c.paint()

    # lines
    c.set_source_rgb(0,0,0)
    c.move_to(50, 100)
    c.line_to(100, 150)
    c.rel_line_to(150, -100)
    c.rel_move_to(-10, -10)
    c.rel_line_to(20, 20)
    c.set_line_width(2)
    c.stroke()
    
    # rectangles
    c.set_line_width(6)
    c.rectangle(300, 50, 100, 50)
    c.stroke()
    
    # arcs
    c.set_source_rgb(1,0,1)
    # x, y, radius, start_angle, stop_angle
    c.arc(200, 180, 40, 0, 2*math.pi)
    c.fill_preserve()
    c.set_line_width(2)
    c.set_source_rgb(0,0,0)
    c.stroke()
    
    surface.write_to_png(filename)
