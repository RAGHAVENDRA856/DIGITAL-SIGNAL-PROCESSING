import numpy as np
p =[[3,4,2],[5,3,4],[2,4,3]]
q =[[6,7,5],[7,4,6],[8,3,2]]
print("original matrix:")
print(p)
print(q)
x=np.dot(p,q)
y= np.cross(p, q)
z= np.cross(q, p)
print("dot product of the given two vectors(p,q):")
print(x)
print("cross product of the said two vectors(p, q):")
print(y)
print("cross product of the said two vectors(q, p):")
print(z)
