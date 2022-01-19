import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

if __name__ == '__main__':
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    d = np.random.randn(10000000, 2)
    N = 50
    density, edges = np.histogramdd(d, bins=[50, 50])
    print("样本总数: ", np.sum(density))
    density = density/density.max()
    x = y = np.arange(N)
    t = np.meshgrid(x,y)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(t[0], t[1], density, c='r', s=15*density, marker='o', depthshade=True)
    ax.plot_surface(t[0], t[1], density, cmap='rainbow', rstride=1, cstride=1, alpha=0.9, lw=1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.title("point cloud for the data set")
    plt.tight_layout(0.1)
    plt.show()
