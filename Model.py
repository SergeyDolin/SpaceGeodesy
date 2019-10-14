from numpy import*
import numpy as np
from scipy import optimize

#Моделирование задачи (Абсолютный метод)
Sat1 = np.array([1000, 1500,11])
Sat2 = np.array([2000, 1500,10])
Sat3 = np.array([1000, 500,17])
Sat4 = np.array([2000, 500,100])
Sat5 = np.array([2020, 400,100])
Satellites = np.array([Sat1, Sat2, Sat3, Sat4, Sat5])
cdt =  0.9999999997
GroundItem = np.array([1550, 680, 5])
X = np.hstack((GroundItem, np.array([ cdt])))
V = np.random.normal(0, 0.1, 5)
E = np.ones((5,1))
sigma = np.array([0.5, 0.5, 0.5])

# Априорная дисперсия единицы веса
sigma_sq = 0.00001
Cov = np.cov(V)
P = np.dot(sigma_sq, Cov)

GroundItemInitialError = np.random.normal(0, 10, 3)

dist1 = np.linalg.norm(Sat1-GroundItem)
dist2 = np.linalg.norm(Sat2-GroundItem)
dist3 = np.linalg.norm(Sat3-GroundItem)
dist4 = np.linalg.norm(Sat4-GroundItem)
dist5 = np.linalg.norm(Sat5-GroundItem)


#Памятка

#A = np.random.rand(5,3)
#X = np.random.rand(3)
#V = np.random.normal(0, 0.1, 5)
#F = np.dot(A, X)
#X_new = np.dot(np.linalg.pinv(A), (F+V))
#V_new = (np.dot(A,X_new)) - F

#def Iterations(self, rho_measured, groundItemApprox):
 #       orts = []
  #      f = []
   #     for i in Satellites:
    #        orts.append((i-groundItemApprox) / np.linalg.norm(i-groundItemApprox))

    #______________________________________________________________
    # ТУТ БУДЕТ УЖАСНЫЙ КОСТЫЛЬ

     #   A1 = np.vstack((orts[0],orts[1],orts[2],orts[3],orts[4]))
      #  A = np.hstack((A1,E))
    
    #______________________________________________________________

      #  for j in range(0, Satellites.__len__()):
       #     f.append(-rho_measured[j] + np.dot(orts[j].transpose(), (Satellites[j])))
    
    #______________________________________________________________
    # И ТУТ ТОЖЕ ОН БУДЕТ    

        #f_ = np.array([f[0],f[1],f[2],f[3],f[4]])

    #______________________________________________________________

    #X_new = np.dot(np.dot(np.linalg.pinv(A),P), f_)
        #X_new = np.dot(np.linalg.pinv(A), f_)
    #print("X estimated", X_new)
        #Xest = np.array([X_new[0],X_new[1],X_new[2]])

        #delta = Xest - groundItemApprox
        #groundItemApprox_1 = groundItemApprox + delta
    #print("First iteration", groundItemApprox_1)
        #return  groundItemApprox_1