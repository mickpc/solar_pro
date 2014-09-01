from django.shortcuts import render

from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import StringIO
from django.http import HttpResponse
from django.template import RequestContext, loader
 

def graph(request):#comment
    x = [1,2,3,4,5,6]
    y = [3,5,6,4,4,4]
    plot(x,y, linewidth=2)
    
    xlabel('x axis')
    ylabel('y axis')
    title('sample graph')
    grid(True)
    
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer,"PNG")
    pylab.close()
    
    return HttpResponse(buffer.getvalue(), mimetype = "image/png")
    