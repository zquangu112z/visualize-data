import matplotlib.pyplot as plt
import numpy as np

def plot2DMatrix(array):
    plt.ylabel('Right labels')
    plt.title('Confusion Matrix')
    plt.imshow(array, origin='upper');
    for i in range(len(array)):
        for j in range(len(array[0])):
            plt.text(i-0.125,j+0.125,array[i][j])

    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    array = [[33,2,0,0,0,0,0,0,0,1,3], 
        [3,31,0,0,0,0,0,0,0,0,0], 
        [0,4,41,0,0,0,0,0,0,0,1], 
        [0,1,0,30,0,6,0,0,0,0,1], 
        [0,0,0,0,38,10,0,0,0,0,0], 
        [0,0,0,3,1,39,0,0,0,0,4], 
        [0,2,2,0,4,1,31,0,0,0,2],
        [0,1,0,0,0,0,0,36,0,2,0], 
        [0,0,0,0,0,0,1,5,37,5,1], 
        [3,0,0,0,0,0,0,0,0,39,0], 
        [0,0,0,0,0,0,0,0,0,0,38]]
    plot2DMatrix(array)