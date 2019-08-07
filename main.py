# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:24:45 2019

@author: roehrenbach
"""



from mb_gui import mb_gui



try:
    mb = mb_gui(400,400,"mandelbrot")
    mb.run()
except:
    mb.terminate()
    print("terminated...")
