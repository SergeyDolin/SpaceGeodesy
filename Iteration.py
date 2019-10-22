from numpy import*
import numpy as np
from scipy import optimize
from Model import*




def Iterations(rho_measured, groundItemApprox):
        orts = []
        f = []


        for i in Satellites:
            orts.append((i-groundItemApprox) / np.linalg.norm(i-groundItemApprox))

        A1 = np.vstack((orts[0],orts[1],orts[2],orts[3],orts[4]))
        A = np.hstack((A1,E))

        for j in range(0, Satellites.__len__()):
            f.append(-rho_measured[j] + np.dot(orts[j].transpose(), (Satellites[j])))

        f_ = np.array([f[0],f[1],f[2],f[3],f[4]])

        sigma_sq = 0.00001

        Cov = np.zeros((f_.__len__(), f_.__len__()), float)
        
        np.fill_diagonal(Cov, Squared_RMS)

        X_new = np.dot((np.linalg.inv(np.dot((A.T),np.dot(Cov,A)))), (np.dot((A.T),np.dot( Cov,f_))))
        #X_new = np.dot(np.dot(np.linalg.pinv(A),P), f_)
        #X_new = np.dot(np.linalg.pinv(A), f_)
        #print("X estimated", X_new)
        Xest = np.array([X_new[0],X_new[1],X_new[2]])

        delta = Xest - groundItemApprox
        groundItemApprox_1 = groundItemApprox + delta
        #print("First iteration", groundItemApprox_1)
        return  groundItemApprox_1