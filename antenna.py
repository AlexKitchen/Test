# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:08:43 2020

@author: alexk
"""

from __future__ import division
import numpy as np
from numpy import pi
import matplotlib.pyplot as pp

# normalize and convert to dB
dbnorm = lambda x: 20*np.log10(np.abs(x)/np.max(x));

# generate example data
# some angles
alpha = np.arange(-90, 190, 0.001);
x = np.deg2rad(alpha)
dir_function = dbnorm((np.cos(x))**2)

# plot
ax = pp.subplot(111, polar=True)
# set zero north
ax.set_theta_zero_location('N')
ax.set_theta_direction('anticlockwise')
pp.plot(np.deg2rad(alpha), dir_function)
ax.set_ylim(-20,0)
ax.set_yticks(np.array([-20, -12, -6, 0]))
ax.set_xticks(np.array([0, -45, -90,90, 45])/180*pi)
pp.show()
