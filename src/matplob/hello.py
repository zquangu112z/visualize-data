import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4]) # y-axis


plt.plot([1,2,3,4], [1,4,9,16], 'b-')
plt.axis([0, 6, 0, 20]) # [xmin, xmax, ymin, ymax]


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)




#----------------Controlling line properties
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')







plt.ylabel('some numbers')
plt.show()