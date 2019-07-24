# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:27:49 2019

@author: jakob
"""



import pygame
from time import time
import numpy as np
from mandelbrot_set import mandelbrot_set


class Command:
    
    def __init__(self, gui=None):
        self.gui = gui
    
    def execute(self, *args):
        print("nothing to execute!")

# example commands
class LMB(Command):
    
    def __init__(self, gui):
        Command.__init__(self, gui)
    
    def execute(self, pos):
        self.gui.mb_x += self.gui.mb_size*(pos[0]/float(self.gui.mb_resolution)-0.5)
        self.gui.mb_y += self.gui.mb_size*(pos[1]/float(self.gui.mb_resolution)-0.5)
        print self.gui.mb_x, self.gui.mb_y
        self.gui.mb_size *= self.gui.zoom_factor
        self.gui._create_mb()
        self.gui.waiting = False



class mb_gui:
    
    def __init__(self, w, h, name=""):
        # initialize pygame and window
        pygame.init()
        self.surf = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        
        # commands for pressed keys/buttons
        self.commands = {
                1: LMB(self) # left mouse button
        }
        self.waiting = False
        
        self.time = time()
        pygame.mouse.set_pos((w/2,h/2))
        
        self.mb_maxiter = 80
        self.mb_size = 2
        self.mb_resolution = w
        self.mb_x, self.mb_y = 0, 0
        self._create_mb()
        self.zoom_factor = 0.5
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.waiting = False
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button not in self.commands:
                    continue
                self.commands[event.button].execute(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "":
                    continue
                if event.unicode not in self.commands:
                    continue
                self.commands[event.unicode].execute()
    
    def _create_mb(self):
        self.mb = mandelbrot_set(
                self.mb_x,
                self.mb_y,
                self.mb_size,
                self.mb_resolution,
                self.mb_maxiter
        )
    
    def _draw_mb(self):
        self.mb = self.mb * 250 / self.mb.max()
        pygame.surfarray.blit_array(self.surf, self.mb)
    
    def _draw(self):
        self._draw_mb()
        pygame.display.update()
    
    def run(self):
        self.running = True
        while self.running:
            while self.waiting:
                self._handle_events()
            self._draw()
            self.waiting = True
        pygame.quit()
    
    def terminate(self):
        pygame.quit()

