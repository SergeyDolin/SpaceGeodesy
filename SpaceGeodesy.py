from numpy import*
import numpy as np
from scipy import optimize
from Model import*
from Iteration import*


#Дано:
rho_measured = np.array([dist1,dist2,dist3,dist4,dist5]) + V #измеренные (псевдо)дальности 
groundItemApprox = GroundItem + GroundItemInitialError #приближенные координаты станции
#и Координаты спутников

#_____________________________
#Решение
#_____________________________

x = Iterations(rho_measured, groundItemApprox)
Delta = x - groundItemApprox
print(x)
while Delta.all() > 0.1:
    x1 = Iterations(rho_measured, x)
    Delta = x1 - x
    print(x1)
    x = Iterations(rho_measured, x1)
#print(Cov)




#print(GroundItem - X_new1)


#deltaX = X_new-X
#print(deltaX)
#F = np.dot(A, X_new)
#X_new1 = np.dot(np.linalg.pinv(A), F)
#print(X_new1)
#V_new = (np.dot(A,X_new)) - F
