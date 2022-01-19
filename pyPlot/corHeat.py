from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

aaa=np.loadtxt('te.csv',delimiter=',')
xlab=['Airplane','Airport','Baseball field','Basketball court','Bridge','Chimney','Dam','ESA','ETS','Golf course','Ground track','Harbor','Overpass','Ship','Stadium','Storage tank','Tennis court','Train station','Vehicle','Wind mill']

mask = np.zeros_like(aaa)
#返回矩阵下三角
# mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(15, 15))
    ax = sns.heatmap(aaa,mask=mask,square=True,xticklabels=xlab, yticklabels=xlab,cmap="rainbow",annot=False,linewidth=0.5)
ax.set_xticklabels(xlab,fontsize=16,rotation=45,horizontalalignment='right')
ax.set_yticklabels(xlab,fontsize=16,horizontalalignment='right')
fig=ax.get_figure()
fig.savefig('C:\\Users\\dd\\Desktop\\cor_heat.png',dpi=1080)
fig.savefig('C:\\Users\\dd\\Desktop\\cor_heat.pdf')