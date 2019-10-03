from numpy import*
import numpy as np
from scipy import optimize

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


#Памятка

#A = np.random.rand(5,3)
#X = np.random.rand(3)
#V = np.random.normal(0, 0.1, 5)
#F = np.dot(A, X)
#X_new = np.dot(np.linalg.pinv(A), (F+V))
#V_new = (np.dot(A,X_new)) - F