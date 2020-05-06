import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


n = 500;  
m = 100;
p_0 = np.linspace(0,2*np.pi,m);
p_r = np.random.rand(m)*2*np.pi;
x_r = np.random.rand(m)*2*np.pi;

def func(K):
    p = np.zeros([m,n]);
    x = np.zeros([m,n]);
    p[:,0] = p_r;
    x[:,0] = x_r;
    for i in range(1,n):
        p[:,i] = (p[:,i-1] + K*np.sin(x[:,i-1])) % (np.pi*2) ;
        x[:,i] = (x[:,i-1] + p[:,i]) % (np.pi*2)
    p = p / (2*np.pi)
    x = (x  % (np.pi*2)) / (2*np.pi)
    return (x,p)

colors = (0,0,0)

K = np.linspace(0,7,70);


fig, ax = plt.subplots()
x, y = [],[]
sc = ax.scatter(x,y,s=0.1)
plt.xlim(0,1)
plt.ylim(0,1)

def animate(i):
    (a,b) = func(K[i])
    a = a.flatten()
    b = b.flatten()
    sc.set_offsets(np.c_[a,b])





ani = animation.FuncAnimation(fig, animate, np.arange(1, len(K)),
                              interval=120,repeat=True)


# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)

# ani.save('SM.mp4',writer=writer)

plt.show()