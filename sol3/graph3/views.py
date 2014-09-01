from django.shortcuts import render

from matplotlib import pylab
from pylab import *

def graph():
    x = [1,2,3,4,5,6]
    y = [3,5,6,4,4,4]
    plot(x,y, linewidth=2)
    
    xlabel('x axis')
    ylabel('y axis')
    title('sample graph')
    grid(True)
    