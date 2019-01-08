import cairo

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 300)
    c = cairo.Context(surface)

    c.set_line_width(5)
    
    c.set_source_rgb(0,0,0)
    
    # 15 drawn, 10 not drawn, etc
    c.set_dash([15, 10])

    c.move_to(50, 50)  
    c.line_to(400, 50)
    c.stroke()

    # 10 drawn, 30 not drawn, 5 drawn, then
    # 10 *not* drawn, 30 drawn, 5 not drawn, etc
    c.set_dash([10, 30, 5])

    c.move_to(50, 100)
    c.line_to(400, 100)
    c.stroke()

    surface.write_to_png(filename)
