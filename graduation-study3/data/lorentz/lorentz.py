#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import math
from tqdm import tqdm


# In[2]:


######################################################

# RK4法
k0=[0,0,0]
k1=[0,0,0]
k2=[0,0,0]
k3=[0,0,0]

def rk4(t, x, y, z, h, tmax):
  x_ap = [x]
  y_ap = [y]
  z_ap = [z]
  t_ap = [t]

  while t <= tmax:
    if t%100 ==0:
      print(t)
    
    k0= h * Lorenz(x, y, z, a1, b1, c1);

    k1= h * Lorenz(x+k0[0]/2.0, y+k0[1]/2.0, z+k0[2]/2.0, a1, b1, c1);

    k2= h * Lorenz(x+k1[0]/2.0, y+k1[1]/2.0, z+k1[2]/2.0, a1, b1, c1); 

    k3= h * Lorenz(x+k2[0], y+k2[1], z+k2[2], a1, b1, c1);

    dx =  (k0[0]+2.0*k1[0]+2.0*k2[0]+k3[0])/6.0;
    dy =  (k0[1]+2.0*k1[1]+2.0*k2[1]+k3[1])/6.0;
    dz =  (k0[2]+2.0*k1[2]+2.0*k2[2]+k3[2])/6.0;


    x = x + dx
    y = y + dy 
    z = z + dz
   # write([t,x,y,z])
    #print(t,x,y)
    t = t + h

    x_ap.append(x)
    y_ap.append(y)
    z_ap.append(z)
    t_ap.append(t)

  return t_ap, x_ap, y_ap, z_ap  
  ######################################################

######################################################
# 微分方程式
def Lorenz(x, y, z, sgm, b, r):  
  x_dot = sgm*(y - x)
  y_dot = r*x - y - x*z
  z_dot = x*y - b*z
  return np.array([x_dot, y_dot, z_dot])

######################################################

t=0

#x0, y0, z0 =[0, 1, 5] 
x0, y0, z0 =[np.random.random(), np.random.random(), np.random.random()] 

a1 = 10 # a is sgm for LORE
b1 = 8/3
c1 = 100

##########################
tmax = 1000  # tの最大値 
##########################
h = 0.0005  # 刻み幅

t_a1, x_a1 , y_a1, z_a1 = rk4(t, x0, y0, z0, h, tmax)
np.save("time", t_a1)
np.save("trackX", x_a1)
np.save("trackY", y_a1)
np.save("trackZ", z_a1)

# fig = plt.figure(figsize=(30,10))
# ax = fig.add_subplot(1,1,1)
# ax.scatter(t_a1, x_a1, c='blue', label='x', s = 0.05)
# ax.scatter(t_a1, y_a1, c='red', label='y', s = 0.05)
# ax.scatter(t_a1, z_a1, c='green', label='z', s = 0.05)

# fig = plt.figure(figsize=(10,10))
# ax = fig.add_subplot(1,1,1)
# plt.plot(x_a1, y_a1, marker='.', markersize=0.05, color="r")
# plt.xlim(np.min(x_a1) - 1, np.max(x_a1) + 1)
# plt.ylim(np.min(y_a1) - 1, np.max(y_a1) + 1)    
# plt.grid(color="0.9", linestyle='-', linewidth=1)
# plt.title("X vs Y")
# #plt.gca().set_aspect('equal')

# fig = plt.figure(figsize=(10,10))
# ax = fig.add_subplot(1,1,1)
# plt.plot(x_a1, z_a1, marker='.', markersize=0.05, color="b") 
# plt.xlim(np.min(x_a1) - 1, np.max(x_a1) + 1)
# plt.ylim(np.min(z_a1) - 1, np.max(z_a1) + 1)    
# plt.grid(color="0.9", linestyle='-', linewidth=1)
# plt.title("X vs Z")
# #plt.gca().set_aspect('equal')

# fig = plt.figure(figsize=(10,10))
# ax = fig.add_subplot(1,1,1)
# plt.plot(y_a1, z_a1, marker='.', markersize=0.05, color="g")
# plt.xlim(np.min(y_a1) - 1, np.max(y_a1) + 1)
# plt.ylim(np.min(z_a1) - 1, np.max(z_a1) + 1)    
# plt.grid(color="0.9", linestyle='-', linewidth=1)
# #plt.gca().set_aspect('equal')
# plt.title("Y vs Z")
# plt.show()





