from numpy import*
import numpy as np
from scipy import optimize
from Model import*

def Iterations(rho_measured, groundItemApprox):
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
    return  groundItemApprox_1
