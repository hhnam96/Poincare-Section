#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:05:28 2019

@author: nhoanghoai
"""

import numpy as np
import matplotlib.pyplot as plt

N = 500; n =10;
t = np.arange(0,N*2*np.pi,2*np.pi/n);
dt = 2*np.pi/n;
m = 240;
p_0 = np.linspace(-2.5,2.5,m);
p = np.zeros([m,n*N]);
x = np.zeros([m,n*N]);
a = 0.1;
p[:,0] = p_0;
n_1 =1; n_2=1;
x_out = np.zeros([m,N])
p_out = np.zeros([m,N]); p_out[:,0] = p_0;
t_out = np.zeros([N])
for i in range(1,len(t)):
	p[:,i] = (p[:,i-1] + a*(n_1*np.sin(x[:,i-1]-t[i-1])+n_2*np.sin(x[:,i-1]+t[i-1]) )*dt) #% (np.pi*2) ;
	x[:,i] = (x[:,i-1] + p[:,i]*dt) #% (np.pi*2)
	if ((i % n) == 0):
		p_out[:,i//n] = p[:,i]
		x_out[:,i//n] = x[:,i]
		t_out[i//n] = t[i]
        
x_out = (x_out)  % (np.pi*2) / (2*np.pi)


colors = (0,0,0)

plt.figure()
for i in range(m):
	plt.scatter(x_out[i,:],p_out[i,:],s=0.02,c=colors)

plt.show()