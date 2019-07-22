# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:21:44 2019

@author: jakob
"""



import numpy as np
from time import time

# numpy compact

# =============================================================================
# def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
#     x = np.linspace(xmin, xmax, width)
#     y = np.linspace(ymin, ymax, height)
#     x,y = np.meshgrid(x,y)
#     c = x + y * 1j
#     z = np.ma.array(c.copy(), mask=np.zeros(c.shape))
#     mset = np.zeros(c.shape, dtype=int)
#     
#     for i in range(maxiter):
#         sel = ~z.mask & (z > 2)
#         mset[sel] = i
#         z.mask |= sel
#         z[~z.mask] = z[~z.mask]**2 + c[~z.mask]
#     
#     return np.where(z.mask, mset, maxiter)
# =============================================================================

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    x,y = np.meshgrid(x,y)
    z = x + y * 1j
    c = np.array(z)
    z = np.ma.array(z, mask=np.zeros(z.shape))
    mset = np.zeros(z.shape, dtype=int)
    
    for i in range(maxiter):
        sel = ~z.mask & (z > 2)
        mset[sel] = i
        z.mask |= sel
        z[~z.mask] = z[~z.mask]**2 + c[~z.mask]
    
    return np.where(z.mask, mset, maxiter)
