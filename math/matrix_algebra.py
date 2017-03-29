# Linear Algebra

import numpy as np

a = np.matrix('1,2,3;2,7,4')
b = np.matrix('1,-1;0,1]')
c = np.matrix('5,-1;9,1;6,0')
d = np.matrix('3,-2,-1;1,2,3')

cT = c.transpose()
aT = a.transpose()


u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

UplusV = u + v
UminusV = u - v
scalar = 6*u
dot = np.dot(u,v)
norm = np.linalg.norm(u)

print('UplusV: ', UplusV)
print('UminusV: ', UminusV)
print('times 6 scalar: ', scalar)
print('dot: ', dot)
print('norm: ', norm)
print('a-cT: ', a-cT)
print('cT + 3d: ', cT + 3*d)
print('b * a: ', b*a)
