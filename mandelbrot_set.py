# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:21:44 2019

@author: jakob
"""

import numpy as np

# standard input
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

def mandelbrot_set(pos,size,resolution,maxiter):
    # NOTE: switched position for im and re because result incorrect
    #       -> investigate later
    im = np.linspace(pos[0]-size/2, pos[0]+size/2, resolution)
    re = np.linspace(pos[1]-size/2, pos[1]+size/2, resolution)
    re,im = np.meshgrid(re,im)
    c = re + im * 1j
    z = np.ma.array(c.copy(), mask=np.zeros(c.shape))
    mset = np.zeros(c.shape, dtype=int)
    
    for i in range(maxiter):
        sel = ~z.mask & (z > 2)
        mset[sel] = i
        z.mask |= sel
        z[~z.mask] = z[~z.mask]**2 + c[~z.mask]
    
    return np.where(z.mask, mset, maxiter)

