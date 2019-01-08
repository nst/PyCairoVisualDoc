import cairo

def draw_line(c):
    c.move_to(10, 10)
    c.line_to(100, 100)
    c.stroke()

def draw_png(filename):

    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(s)
    
    c.set_source_rgb(1,0,0)
    draw_line(c)
    
    # invert y coordinates
    m = cairo.Matrix(yy=-1, y0=s.get_height())
    c.transform(m)
    
    c.set_source_rgb(0,0,1)
    draw_line(c)
    
    s.write_to_png(filename)

if __name__ == "__main__":

    draw()
