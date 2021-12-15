import pandas as pd
import scipy as sp
from matplotlib import pyplot as plt
from scipy.stats import stats


def ex_2_Fisher():
    '''Визуализация разных F-распределений на графике'''
    mu = 0
    d1_values, d2_values = [4, 9, 49], [95, 90, 50]
    linestyles = ['-', '--', ':', '-.']
    x = sp.linspace(0, 5, 101)[1:]
    ax = None
    for (d1, d2, ls) in zip(d1_values, d2_values, linestyles):
        dist = stats.f(d1, d2, mu)
        df  = pd.DataFrame( {0:x, 1:dist.pdf(x)} )
        ax = df.plot(0, 1, ls=ls,
                     label=r'$d_1=%i,\ d_2=%i$' % (d1,d2), ax=ax)
    plt.xlabel('$x$\nF-статистика')
    plt.ylabel('Плотность вероятности \n$p(x|d_1, d_2)$')
    plt.show()