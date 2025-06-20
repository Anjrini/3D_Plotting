# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 15:25:40 2025

@author: Mustafa Anjrini
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def plot_values(x,y,func):
    l=len(x)
    m_x=np.zeros((l,l))
    m_y=np.zeros((l,l))
      
    for i in range(l):
        m_x[:,i]=x[i]
        m_y[i,:]=y[i]
    
    x=m_x
    y=m_y
    z=func(x,y)
    
    return x,y,z

def func(x,y):
    return x**3-6*x*y+y**3

x= np.arange(-4,4,0.1)
y= np.arange(-4,4,0.1)

#z=np.sin(np.sqrt(x**2+y**2))

x,y,z=plot_values(x, y, func)

# 3D plotting
fig=plt.figure()
ax=fig.add_subplot(projection="3d")
ax.plot_surface(x,y,z,cmap=cm.coolwarm,linewidth=0)
fig.subplots_adjust(top=1.1, bottom=-.1)
#ax.plot_wireframe(x,y,z)

ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_zlabel("z values")
ax.view_init(azim=15,elev=10)
fig    

