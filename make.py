import pkgutil
import inspect
import cairo
import math
import os
import re

from operator import attrgetter
from time import strftime

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from cairo import SVGSurface, PDFSurface

def get_submodules(mod):
    
    l = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(mod.__path__, mod.__name__+'.'):
        if not is_pkg:
            l.append(__import__(module_name, fromlist='xxx'))
    return sorted(l, key=attrgetter('__name__'))

def call_drawing_function(f):

    m = re.match("draw_(png|svg|pdf|gif|ps|eps).*", f.__name__)
    
    if not m:
        print("xx", f.__name__)
        return None
    
    print("-- %s()" % f.__name__)
    
    mod_comps = mod.__name__.split(".")
    dir_comps = ["img"] + mod_comps[1:-1]
    directory = os.path.sep.join(dir_comps)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    ext = m.groups()[0]
    
    image_name = "%s.%s" % (os.path.sep.join([directory, mod_comps[2]]), ext)
                    
    f(image_name)
    
    return image_name    

def path_items(mod):

    comps = mod.__name__.split(".")

    d = {}
    d["id"] = ".".join(comps[1:])
    d["title"] = ".".join(comps[1].split("_")[1:]).capitalize()
    d["filename"] = comps[-1] + ".py"
    d["filepath"] = os.path.sep.join(comps) + ".py"
    d["filename_with_parent_dir"] = os.path.sep.join(comps[-2:]) + ".py"

    return d

if __name__ == "__main__":

    """
    Create an HTML file with snippets source code + images.
    
    Images are generated for all modules according to functions names.
    
    Optional code delimiters: "# BEGIN" and "# END".
    """
    
    s = ""

    modules = get_submodules(__import__('snippets'))
    
    sections = {}
    
    for mod in modules:
        name = mod.__name__.split(".")[1]
        sections.setdefault(name, []).append(mod)
    
    s += "<h4>Content</h4>\n"

    s += "<ol>\n"
    for name, mods in sorted(iter(sections.items())):
        s += '<li>%s\n' % " ".join(name.split("_")[1:]).capitalize()
        s += "<ul>\n"
        for mod in mods:
            d = path_items(mod)
            s += '<li><a href="#%s">%s</a></li>\n' % (d["id"], d["filename"])
        s += "</ul>\n</li>\n"
    s += "</ol>\n"
    
    s += '<table>\n'
    
    for mod in modules:
        
        d = path_items(mod)
        
        s += '<tr id="%s">\n' % d["id"]
        s += '<td>\n'
        
        functions = [o for n,o in inspect.getmembers(mod) if inspect.isfunction(o)]
        
        module_and_functions = []
        
        for f in functions:
            
            image_name = call_drawing_function(f)
            
            if image_name != None:                                
                _, ext = os.path.splitext(image_name)
                if ext in [".pdf", ".ps", ".eps"]:
                    s += '<a href="%s">%s</a>\n' % (image_name, os.path.basename(image_name))
                else:
                    s += '<img src="%s" alt="%s"/>\n' % (image_name, d["id"])                    

        s += "</td>\n"
        
        # add source code to HTML
        
        with open(d["filepath"]) as f:  
            code = f.read()
        
        if "# BEGIN" in code and "# END" in code:
            # TODO: use regex, allow several chunks
            code = code.split("# BEGIN")[1].lstrip("\n").split("# END")[0].rstrip()

        s += '<td>\n'

        s += "<code><b>/%s</b></code>\n" % d["filename_with_parent_dir"]

        hightlighted_code = highlight(code, PythonLexer(), HtmlFormatter())
        
        s += "%s\n" % hightlighted_code

        s += "</td>\n"
        s += "</tr>\n"
        
    s += "</table>\n"

    with open("template.html", "r") as f:
        template = f.read()

    d = {"pycairo_version": cairo.cairo_version_string(), "content": s, "date": strftime("%Y-%m-%d %H:%M:%S")}
        
    html = template.format(**d)

    with open("index.html", "w") as f:
        f.write(html)
