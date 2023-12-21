import matplotlib.pyplot as plt

x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[25,16,9,4,1,0,1,4,9,16,25]
x2=np.linspace(-5,5,100)
y2=x2**2
plt.plot(x,y)
plt.plot(x2,y2)
plt.plot(x2,-y2)
plt.show()