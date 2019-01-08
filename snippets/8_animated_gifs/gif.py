import os
import imageio

def images_paths():
    # ensure we can read images when working from another dir
    cwd = os.getcwd()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    files = [os.path.sep.join([dir_path, s])
             for s in os.listdir(dir_path)
             if s.endswith('.png')]
    files.sort()
    os.chdir(cwd)
    return files

def draw_gif(filename):

    images = []
    
    for s in images_paths():
        images.append(imageio.imread(s))
    
    imageio.mimsave(filename, images, format='GIF', duration=0.5)

if __name__ == "__main__":

    draw_gif("movie.gif")
