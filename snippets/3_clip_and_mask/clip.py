import cairo
import math
import os

def create_from_png(image_name):
    # ensure we can read image when working from another dir
    cwd = os.getcwd()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    ims = cairo.ImageSurface.create_from_png(image_name)
    os.chdir(cwd)
    return ims

def draw_png(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
    c = cairo.Context(surface)

    ims = create_from_png("church.png")
    
    # BEGIN
    c.arc(100, 100, 75, 0, 2*math.pi)
    
    c.save()
    c.clip()
    c.set_source_surface(ims, 0, 0)    
    c.paint()
    c.restore()

    c.set_source_surface(ims, 256, 0)    
    c.paint()
    # END
    
    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_png("clip.png")
