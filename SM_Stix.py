#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:05:28 2019

@author: nhoanghoai
"""

import numpy as np
import matplotlib.pyplot as plt

l = 4.; W = 3.;
e = 1/30.; 


N = 1000; 
P = 2*np.pi/W;
n = 60;
dt = P/n;
t = np.arange(0,N*P,dt);
m = 500;

sigma = 0.05
p_i = np.random.normal(0,sigma,500)
x_i = np.random.normal(0,sigma,500)

# p_i = np.linspace(-0.1,0.1,m);
# p_i = np.random.random(m)*.001
# x_i = np.linspace(-np.pi,np.pi,m);
p = np.zeros([m,n*N]);
x = np.zeros([m,n*N]);
p[:,0] = p_i;
x[:,0] = x_i;

n_1 =1; n_2=1;
x_out = np.zeros([m,N])
p_out = np.zeros([m,N]); p_out[:,0] = p_i;
t_out = np.zeros([N])
for i in range(1,len(t)):
	p[:,i] = (p[:,i-1] - (n_1*np.sin(x[:,i-1])+n_2*e*l*np.sin(l*x[:,i-1]-W*t[i-1]) )*dt) #% (np.pi*2) ;
	x[:,i] = (x[:,i-1] + p[:,i]*dt) #% (np.pi*2)
	if ((i % n) == 0):
		p_out[:,int(i/n)] = p[:,i]
		x_out[:,int(i/n)] = x[:,i]
		t_out[int(i/n)] = t[i]
        
x_out = (x_out)  % (np.pi*2) / (2*np.pi)
for i in range(x_out.shape[0]):
	for j in range(x_out.shape[1]):
		if x_out[i,j] > 0.5:
			x_out[i,j] = x_out[i,j] - 1



# p_out = p_out*l/W

colors = (0,0,0)

plt.figure()
for i in range(m):
	plt.scatter(x_out[i,:],p_out[i,:],s=0.01)

# plt.savefig('myfig.svg')
plt.show()