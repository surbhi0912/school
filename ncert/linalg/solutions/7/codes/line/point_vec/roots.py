import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-11,4,100)
p=np.poly1d([1,6,-27])
for i in range(len(x)):
    y=p(x)

roots=p.r
A=np.array([roots[0],0])
B=np.array([roots[1],0])
print(A,B)
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.5), B[1] * (1-0.1) , 'B')
plt.plot(x,y)
plt.xlim(-15,5)
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show() 