from numpy import*
import numpy as np
from scipy import optimize
from Model import*
from Iteration import*


#Дано:
rho_measured = np.array([dist1,dist2,dist3,dist4])  + V #измеренные (псевдо)дальности 
groundItemApprox = GroundItem + GroundItemInitialError #приближенные координаты станции
#и Sat1, Sat2, Sat3, Sat4 (Координаты спутников)
sigma = np.array([0.5, 0.5, 0.5])
#_____________________________
#Решение
#_____________________________

x = Iterations(rho_measured, groundItemApprox)
delta = x - groundItemApprox
while not delta.all() < sigma.all():
    if delta.all() < sigma.all():
        print(x1)
        break
    x1 = Iterations(rho_measured, x)
    delta = x1 - x

    
    
    




#print(GroundItem - X_new1)


#deltaX = X_new-X
#print(deltaX)
#F = np.dot(A, X_new)
#X_new1 = np.dot(np.linalg.pinv(A), F)
#print(X_new1)
#V_new = (np.dot(A,X_new)) - F
