# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""



import pygame
from time import time
import numpy as np
from mandelbrot_set import mandelbrot_set


# awesome coordinates:
# [0.00993743, 0.28332225] 2.9103830456733704e-11

class Command:
    
    def __init__(self, gui=None):
        self.gui = gui
    
    def execute(self, *args):
        print("nothing to execute!")

# example commands
class LMB(Command):
    
    def __init__(self, gui):
        Command.__init__(self, gui)
    
    def execute(self):
        self.gui.mb_pos = self.gui._get_mb_pos()
        self.gui.mb_size *= self.gui.zoom_factor
        self.gui._create_mb()
        self.gui.drawing = True

class RMB(Command):
    
    def __init__(self, gui):
        Command.__init__(self, gui)
    
    def execute(self):
        print(self.gui._get_mb_pos())


class mb_gui:
    
    def __init__(self, w, h, name=""):
        # initialize pygame and window
        self.screen_mode = "both"
        pygame.init()
        if self.screen_mode == "both":
            self.surf = pygame.display.set_mode((w*2, h))
        else:
            self.surf = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        
        # commands for pressed keys/buttons
        self.commands = {
                1: LMB(self), # left mouse button
                3: RMB(self)
        }
        self.drawing = True
        
        self.time = time()
        self.ms_per_frame = 100
        pygame.mouse.set_pos((w/2,h/2))
        
        self.mb_maxiter = 80
        self.mb_size = 2
        self.mb_resolution = w
        self.mb_pos = np.array([0, 0])
        self._create_mb()
        self.zoom_factor = 0.5
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button not in self.commands:
                    continue
                self.commands[event.button].execute()
# =============================================================================
#             elif event.type == pygame.MOUSEMOTION:
#                 print(self._get_mb_pos())
# =============================================================================
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "":
                    continue
                if event.unicode not in self.commands:
                    continue
                self.commands[event.unicode].execute()
    
    def _get_mb_pos(self):
        pos = np.array(pygame.mouse.get_pos()) / self.mb_resolution
        #print(pos, end=" -> ")
        return self.mb_pos + self.mb_size * (pos - 0.5)
    
    def _create_mb(self):
        if hasattr(self, "mb"):
            self.mb_old = self.mb.copy()
        self.mb = mandelbrot_set(
                self.mb_pos,
                self.mb_size,
                self.mb_resolution,
                self.mb_maxiter
        )
    
    def _get_rgb_array(self, array, c1=(20,0,10), c2=(40,200,10), steps=16):
        r = np.linspace(c1[0], c2[0], steps, dtype=int)
        g = np.linspace(c1[1], c2[1], steps, dtype=int)
        b = np.linspace(c1[2], c2[2], steps, dtype=int)
        i = array % steps
        return np.transpose([r[i], g[i], b[i]],[1,2,0])
    
    def _draw_mb(self):
        screen = self._get_rgb_array(self.mb)
        if self.screen_mode=="both":
            if hasattr(self, "mb_old"):
                mb_old_rgb = self._get_rgb_array(self.mb_old)
            else:
                mb_old_rgb = np.zeros(screen.shape, int)
            screen = np.concatenate([screen, mb_old_rgb])
        
        pygame.surfarray.blit_array(self.surf, screen)
        self.drawing = False
    
    def _draw(self):
        if not self.drawing:
            return
        self._draw_mb()
        pygame.display.update()
        
    def _balance(self, PRINT_SHIFT=False):
        shift = round((time() - self.time) * 1000)
        if PRINT_SHIFT: print(shift)
        if shift<self.ms_per_frame:
            pygame.time.delay(int(self.ms_per_frame - shift))
        self.time = time()
    
    def run(self):
        self.running = True
        while self.running:
            self._handle_events()
            self._draw()
            self._balance()
        pygame.quit()
    
    def terminate(self):
        pygame.quit()



