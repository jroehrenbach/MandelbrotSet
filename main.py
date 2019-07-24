# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:24:45 2019

@author: roehrenbach
"""



from mb_gui import mb_gui


mb = mb_gui(400,400,"mandelbrot")

try:
    mb.run()
    mbs = mb.mb
except:
    mb.terminate()
    print("terminated...")
