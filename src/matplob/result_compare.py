import matplotlib.pyplot as plt
import numpy as np

x_axis = np.array([0,1,2,3,4,5,6,7,8,9])

#RECALL
plt.figure("recall")
#w2v:
recall_w2v = np.array([0.433, 0.858, 0.847, 0.868, 0.865, 0.87, 0.912,0.522, 0.49, 0.478])
# w2v+c2v:
recall_w2v_c2v = np.array([0.79, 0.852, 0.848, 0.873,0.918,0.93,0.922,0.757,0.648,0.643])
# w2v+naive:
recall_w2v_naive = np.array([0.78, 0.868,0.935,0.876, 0.933,0.933,0.935,0.622,0.63,0.635]) 
# c2v:
recall_c2v = np.array([0.583,0.663,0.661,0.738,0.657,0.737,0.595,0.588,0.602,0.572])
# naive:
recall_naive = np.array([0.378, 0.56,0.588,0.61,0.585,0.565,0.432,0.333, 0.333, 0.333])

# plt.subplot(211)
plt.plot(x_axis, recall_w2v, 'k:', label='w2v')
plt.plot(x_axis, recall_w2v_c2v, 'r-.', label='w2v_c2v')
plt.plot(x_axis, recall_w2v_naive, 'm--', label='w2v_naive')
plt.plot(x_axis, recall_c2v, 'bo-', label='c2v')
plt.plot(x_axis, recall_naive, 'gs-', label='naive')

plt.axis([0, 10, 0.2, 1.]) # [xmin, xmax, ymin, ymax]
plt.ylabel('Recall')
plt.xlabel('Number of hidden layer')
plt.legend()

#PRECESION
plt.figure("precesion")
#w2v:
precesion_w2v = np.array([0.628, 0.918, 0.925, 0.917, 0.917, 0.888, 0.88, 0.516, 0.463, 0.442])
# w2v+c2v:
precesion_w2v_c2v = np.array([0.877, 0.933, 0.933, 0.927,0.888,0.863,0.892, 0.791, 0.557, 0.55]) #0.877, 0.933, 0.933, 0.927,0.888,0.863,0.892, nan, nan,nan
# w2v+naive:
precesion_w2v_naive = np.array([0.892, 0.935,0.888,0.9333,0.895,0.898, 0.865, 0.547,0.542, 0.53]) #, nan, nan,nan
# c2v:
precesion_c2v = np.array([0.763,0.915,0.907,0.838,0.908,0.842, 0.427, 0.32, 0.315, 0.317]) #0.763,0.915,0.907,0.838,0.908,0.842,nan,nan,nan,nan
# naive:
precesion_naive = np.array([0.687, 0.943,0.938,0.895, 0.772, 0.548, 0.413, 0.318, 0.355, 0.318 ]) #nan, 0.943,0.938,0.895,nan,nan,nan,nan,nan,nan

# plt.subplot(212)
plt.plot(x_axis, precesion_w2v, 'k:', label='w2v')
plt.plot(x_axis, precesion_w2v_c2v, 'r-.', label='w2v_c2v')
plt.plot(x_axis, precesion_w2v_naive, 'm--', label='w2v_naive')
plt.plot(x_axis, precesion_c2v, 'bo-', label='c2v')
plt.plot(x_axis, precesion_naive, 'gs-', label='naive')

plt.axis([0, 10, 0.3, 1.]) # [xmin, xmax, ymin, ymax]
plt.ylabel('Precision')
plt.xlabel('Number of hidden layer')

plt.legend()
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x_axis = np.array([0,1,2,3,4,5,6,7,8,9])

# #RECALL
# plt.figure("recall")
# # w2v+c2v:
# recall_w2v_c2v = np.array([0.79, 0.852, 0.848, 0.873,0.918,0.93,0.922,0.757,0.648,0.643])
# # w2v+naive:
# recall_w2v_naive = np.array([0.78, 0.868,0.935,0.876, 0.933,0.933,0.935,0.622,0.63,0.635]) 
# # c2v:
# recall_c2v = np.array([0.583,0.663,0.661,0.738,0.657,0.737,0.595,0.588,0.602,0.572])
# # naive:
# recall_naive = np.array([0.378, 0.56,0.588,0.61,0.585,0.565,0.432,0.333, 0.333, 0.333])

# # plt.subplot(211)
# plt.plot(x_axis, recall_w2v_c2v, 'r--', label='w2v_c2v')
# plt.plot(x_axis, recall_w2v_naive, 'y--', label='w2v_naive')
# plt.plot(x_axis, recall_c2v, 'b--', label='c2v')
# plt.plot(x_axis, recall_naive, 'g--', label='naive')

# plt.axis([0, 10, 0.2, 1.]) # [xmin, xmax, ymin, ymax]
# plt.ylabel('Recall')
# plt.xlabel('Number of hidden layer')
# plt.legend()

# #PRECESION
# plt.figure("precesion")
# # w2v+c2v:
# precesion_w2v_c2v = np.array([0.877, 0.933, 0.933, 0.927,0.888,0.863,0.892]) #0.877, 0.933, 0.933, 0.927,0.888,0.863,0.892, nan, nan,nan
# # w2v+naive:
# precesion_w2v_naive = np.array([0.892, 0.935,0.888,0.9333,0.895,0.898, 0.865]) #, nan, nan,nan
# # c2v:
# precesion_c2v = np.array([0.763,0.915,0.907,0.838,0.908,0.842]) #0.763,0.915,0.907,0.838,0.908,0.842,nan,nan,nan,nan
# # naive:
# precesion_naive = np.array([0.943,0.938,0.895]) #nan, 0.943,0.938,0.895,nan,nan,nan,nan,nan,nan

# # plt.subplot(212)
# plt.plot(x_axis[:7], precesion_w2v_c2v, 'r--', label='w2v_c2v')
# plt.plot(x_axis[:7], precesion_w2v_naive, 'y--', label='w2v_naive')
# plt.plot(x_axis[:6], precesion_c2v, 'b--', label='c2v')
# plt.plot(x_axis[1:4], precesion_naive, 'g--', label='naive')

# plt.axis([0, 10, 0.7, 1.]) # [xmin, xmax, ymin, ymax]
# plt.ylabel('Precision')
# plt.xlabel('Number of hidden layer')

# plt.legend()
# plt.show()