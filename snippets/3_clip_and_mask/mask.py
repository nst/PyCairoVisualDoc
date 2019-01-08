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

    # draw mask alone
    mask_img = create_from_png('mask.png')  
    c.set_source_surface(mask_img, 0, 0)
    c.paint()
    
    church_img = create_from_png('church.png')  
    c.set_source_surface(church_img, 256, 0)
    c.paint()
    
    # clip masking area
    c.rectangle(256, 0, church_img.get_width(), church_img.get_height())
    c.clip()
    
    # apply mask
    c.set_operator(cairo.OPERATOR_DEST_IN)
    c.set_source_surface(mask_img, 256, 0)
    c.paint()
    
    surface.write_to_png(filename)

if __name__ == "__main__":

    draw_png("masked_church.png")
