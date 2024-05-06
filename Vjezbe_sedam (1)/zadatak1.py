import particle as par
import projectile as pro
import math as m
import matplotlib.pyplot as plt

proj=par.cestica(45,0,5,20,0.0001)
proj.plot_trajectory()

part=pro.cestica(45,0,5,20,0.01,0.05,0.4,3.5,10)
part.plot_trajectory()
part.graf_kuta()
plt.show()