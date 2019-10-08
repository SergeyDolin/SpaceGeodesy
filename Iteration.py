from numpy import*
import numpy as np
from scipy import optimize
from Model import*

def Iterations(rho_measured, groundItemApprox):
    orts = []
    f = []
    for i in Satellites:
        orts.append((i-groundItemApprox) / np.linalg.norm(i-groundItemApprox))

    #______________________________________________________________
    # ТУТ БУДЕТ УЖАСНЫЙ КОСТЫЛЬ

    A1 = np.vstack((orts[0],orts[1],orts[2],orts[3]))
    A = np.hstack((A1,E))
    
    #______________________________________________________________

    for j in range(0, Satellites.__len__()):
        f.append(-rho_measured[j] + np.dot(orts[j].transpose(), (Satellites[j])))
    
    #______________________________________________________________
    # И ТУТ ТОЖЕ ОН БУДЕТ    

    f_ = np.array([f[0],f[1],f[2],f[3]])

    #______________________________________________________________

    X_new = np.dot(np.linalg.pinv(A), f_)
    print("X estimated", X_new)
    Xest = np.array([X_new[0],X_new[1],X_new[2]])

    delta = Xest - groundItemApprox
    groundItemApprox_1 = groundItemApprox + delta
    #print("First iteration", groundItemApprox_1)
    return  groundItemApprox_1
