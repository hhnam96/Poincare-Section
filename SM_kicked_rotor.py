import numpy as np
import matplotlib.pyplot as plt

n = 1000;  
m = 40;
p_0 = np.linspace(-np.pi,np.pi,m);
p = np.zeros([m,n]);
x = np.zeros([m,n]);
K = 1.2;

p[:,0] = p_0;

for i in range(1,n):
	p[:,i] = (p[:,i-1] + K*np.sin(x[:,i-1])) #% (np.pi*2) ;
	x[:,i] = (x[:,i-1] + p[:,i]) #% (np.pi*2)
x1 = x;	
p = p/ np.pi
x = x  % (np.pi*2)
x = x / (2*np.pi)
colors = (0,0,0)
plt.figure()
for i in range(m):
	plt.scatter(x[i,:],p[i,:],s=0.01,c=colors)

plt.show()