from numpy import*
import numpy as np
from scipy import optimize

#A = np.random.rand(5,3)
#X = np.random.rand(3)
#V = np.random.normal(0, 0.1, 5)
#F = np.dot(A, X)
#X_new = np.dot(np.linalg.pinv(A), (F+V))
#V_new = (np.dot(A,X_new)) - F

#Моделирование задачи (Абсолютный метод)
Sat1 = np.array([1000, 1500,11])
Sat2 = np.array([2000, 1500,10])
Sat3 = np.array([1000, 500,17])
Sat4 = np.array([2000, 500,100])
cdt =  0.9999999997
GroundItem = np.array([1550, 680, 5])
X = np.hstack((GroundItem, np.array([ cdt])))
V = np.random.normal(0, 0.1, 4)
E = np.ones((4,1))


GroundItemInitialError = np.random.normal(0, 10, 3)

dist1 = np.linalg.norm(Sat1-GroundItem)
dist2 = np.linalg.norm(Sat2-GroundItem)
dist3 = np.linalg.norm(Sat3-GroundItem)
dist4 = np.linalg.norm(Sat4-GroundItem)
#Дано:
rho_measured = np.array([dist1,dist2,dist3,dist4])  + V #измеренные (псевдо)дальности 
groundItemApprox = GroundItem + GroundItemInitialError #приближенные координаты станции
#и Sat1, Sat2, Sat3, Sat4 (Координаты спутников)

#_____________________________
#Решение
#_____________________________


#Определене единичных векторов топоцентрического направления на спутник
#______________________________________________________________________
u1 = (Sat1-groundItemApprox) / np.linalg.norm(Sat1-groundItemApprox)
u2 = (Sat2-groundItemApprox) / np.linalg.norm(Sat2-groundItemApprox)
u3 = (Sat3-groundItemApprox) / np.linalg.norm(Sat3-groundItemApprox)
u4 = (Sat4-groundItemApprox) / np.linalg.norm(Sat4-groundItemApprox)
A1 = np.vstack((u1,u2,u3,u4))
A = np.hstack((A1,E))

f_1 =  -rho_measured[0] + np.dot(u1.transpose(), (Sat1))
f_2 =  -rho_measured[1] + np.dot(u2.transpose(), (Sat2))
f_3 =  -rho_measured[2] + np.dot(u3.transpose(), (Sat3))
f_4 =  -rho_measured[3] + np.dot(u4.transpose(), (Sat4))

f_ = np.array([f_1,f_2,f_3,f_4])

X_new = np.dot(np.linalg.pinv(A), f_)
print("X estimated", X_new)
Xest = np.array([X_new[0],X_new[1],X_new[2]])

delta = Xest - groundItemApprox
groundItemApprox_1 = groundItemApprox + delta
print("First iteration", groundItemApprox_1)

#_______________________________________________________________________
u1_1 = (Sat1-groundItemApprox_1) / np.linalg.norm(Sat1-groundItemApprox_1)
u2_2 = (Sat2-groundItemApprox_1) / np.linalg.norm(Sat2-groundItemApprox_1)
u3_3 = (Sat3-groundItemApprox_1) / np.linalg.norm(Sat3-groundItemApprox_1)
u4_4 = (Sat4-groundItemApprox_1) / np.linalg.norm(Sat4-groundItemApprox_1)
A1_1 = np.vstack((u1_1,u2_2,u3_3,u4_4))
A2 = np.hstack((A1_1,E))

f_11 =  -rho_measured[0] + np.dot(u1_1.transpose(), (Sat1))
f_22 =  -rho_measured[1] + np.dot(u2_2.transpose(), (Sat2))
f_33 =  -rho_measured[2] + np.dot(u3_3.transpose(), (Sat3))
f_44 =  -rho_measured[3] + np.dot(u4_4.transpose(), (Sat4))

f_n1 = np.array([f_11,f_22,f_33,f_44])

X_new1 = np.dot(np.linalg.pinv(A2), f_n1)
print("X estimated", X_new1)

Xest1 = np.array([X_new1[0],X_new1[1],X_new1[2]])
delta1 = Xest1 - groundItemApprox_1
groundItemApprox_2 = groundItemApprox_1 + delta1
print("Second iteration", groundItemApprox_2)
#________________________________________________________________________
u1_ = (Sat1-groundItemApprox_2) / np.linalg.norm(Sat1-groundItemApprox_2)
u2_ = (Sat2-groundItemApprox_2) / np.linalg.norm(Sat2-groundItemApprox_2)
u3_ = (Sat3-groundItemApprox_2) / np.linalg.norm(Sat3-groundItemApprox_2)
u4_ = (Sat4-groundItemApprox_2) / np.linalg.norm(Sat4-groundItemApprox_2)
A1_ = np.vstack((u1_,u2_,u3_,u4_))
A3 = np.hstack((A1_,E))

f_111 =  -rho_measured[0] + np.dot(u1_.transpose(), (Sat1))
f_222 =  -rho_measured[1] + np.dot(u2_.transpose(), (Sat2))
f_333 =  -rho_measured[2] + np.dot(u3_.transpose(), (Sat3))
f_444 =  -rho_measured[3] + np.dot(u4_.transpose(), (Sat4))

f_n2 = np.array([f_111,f_222,f_333,f_444])

X_new2 = np.dot(np.linalg.pinv(A3), f_n2)
print("X estimated", X_new2)

Xest2 = np.array([X_new2[0],X_new2[1],X_new2[2]])
delta2 = Xest2 - groundItemApprox_2
groundItemApprox_3 = groundItemApprox_2 + delta2
print("Third iteration", groundItemApprox_3)
#________________________________________________________________________


#print(GroundItem - X_new1)


#deltaX = X_new-X
#print(deltaX)
#F = np.dot(A, X_new)
#X_new1 = np.dot(np.linalg.pinv(A), F)
#print(X_new1)
#V_new = (np.dot(A,X_new)) - F
