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
rho_measured = np.array([dist1,dist2,dist3,dist4]) + cdt + V #измеренные (псевдо)дальности 
groundItemApprox = GroundItem + GroundItemInitialError #приближенные координаты станции
#и Sat1, Sat2, Sat3, Sat4 (Координаты спутников)

#_____________________________
#Решение
#_____________________________



#Определене единичных векторов топоцентрического направления на спутник
u1 = (Sat1-groundItemApprox) / np.linalg.norm(Sat1-groundItemApprox)
u2 = (Sat2-groundItemApprox) / np.linalg.norm(Sat2-groundItemApprox)
u3 = (Sat3-groundItemApprox) / np.linalg.norm(Sat3-groundItemApprox)
u4 = (Sat4-groundItemApprox) / np.linalg.norm(Sat4-groundItemApprox)
A1 = np.vstack((u1,u2,u3,u4))
#A = np.hstack((A1,E))
print(A1)
#Xg = np.hstack((groundItemApprox, np.array([ cdt])))

f_ =  np.dot(A1, groundItemApprox)
X_new = np.dot(np.linalg.pinv(A1), f_)
print(X_new)

deltaX = groundItemApprox - X_new
print(deltaX)
u1_1 = (Sat1-deltaX) / np.linalg.norm(Sat1-deltaX)
u2_2 = (Sat2-deltaX) / np.linalg.norm(Sat2-deltaX)
u3_3 = (Sat3-deltaX) / np.linalg.norm(Sat3-deltaX)
u4_4 = (Sat4-deltaX) / np.linalg.norm(Sat4-deltaX)
A1_1 = np.vstack((u1_1,u2_2,u3_3,u4_4))
#A = np.hstack((A1,E))
print(A1_1)
#Xg1 = np.hstack((groundItemApprox, np.array([ cdt])))

F =  np.dot(A1_1, X_new)
X_new1 = np.dot(np.linalg.pinv(A1_1), F)
print(X_new1)



#deltaX = X_new-X
#print(deltaX)
#F = np.dot(A, X_new)
#X_new1 = np.dot(np.linalg.pinv(A), F)
#print(X_new1)
#V_new = (np.dot(A,X_new)) - F

