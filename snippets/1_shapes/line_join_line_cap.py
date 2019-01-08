import cairo

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 300)
    c = cairo.Context(surface)
    
    c.set_line_width(20)
    
    c.move_to(50, 100)
    c.rel_line_to(50, -50)
    c.rel_line_to(50, 50)
    c.set_line_join(cairo.LINE_JOIN_MITER) # default
    c.stroke()
    
    c.move_to(50, 150)
    c.rel_line_to(50, -50)
    c.rel_line_to(50, 50)
    c.set_line_join(cairo.LINE_JOIN_BEVEL)
    c.stroke()

    c.move_to(50, 200)
    c.rel_line_to(50, -50)
    c.rel_line_to(50, 50)
    c.set_line_join(cairo.LINE_JOIN_ROUND)
    c.stroke()

    c.move_to(200, 50)
    c.rel_line_to(0, 150)
    c.set_line_cap(cairo.LINE_CAP_BUTT)
    c.stroke()

    c.move_to(240, 50)
    c.rel_line_to(0, 150)
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.stroke()

    c.move_to(280, 50)
    c.rel_line_to(0, 150)
    c.set_line_cap(cairo.LINE_CAP_SQUARE)
    c.stroke()

    c.rectangle(350, 50, 100, 100)        
    c.set_line_join(cairo.LINE_JOIN_ROUND)
    c.stroke()
    
    surface.write_to_png(filename)
