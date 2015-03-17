import numpy as np
import scipy as sp 
import math
import pylab as pl
from PyQt4 import QtGui

QtGui.QApplication.setLibraryPaths([]) #workaround for KDE and Anaconda

data = np.loadtxt("rohr1.dat")

print "Mittelwert: ", sp.mean(data)
print "Varianz: ", sp.var(data)

pl.hist(data, 50)
pl.show()
pl.savefig(hist.png)

data2 = np.loadtxt("rohr2.dat", unpack=True)

print "Mittelwert x:", sp.mean(data2[0])
print "Mittelwert y:", sp.mean(data2[1])

std_x = math.sqrt(sp.var(data2[0]))
std_y = math.sqrt(sp.var(data2[1]))

cor_x_y = sp.cov(data2)[0][1] / (std_x * std_y) 

print "Standardabweichung x:", std_x
print "Standardabweichung y:", std_y

print "Korrelation von x und y: ", cor_x_y

pl.scatter(data2[0], data2[1])
pl.show()
pl.savefig(scatter.png)